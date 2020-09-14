import jwt
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
from utils.crypto import md5, encode_jwt, decode_jwt

from db import DBSession
from db.entities import DBUser

from rpc.gen.akun.auth.ttypes import TLoginError, TLoginErrorCode, TAuthError, TAuthErrorCode
from rpc.gen.akun.auth.constants import T_USER_ROLE_DOUBLES
from .manager import get_model
# MODELS MUST ONLY USE THRIFT ENUM AND EXCEPTIONS
# MODELS MAY NOT USE THRIFT STRUCTS

load_dotenv()

AUTH_ENC_FILE = os.getenv("AUTH_ENC")
AUTH_DEC_FILE = os.getenv("AUTH_DEC")
AUTH_SECRET = os.getenv("AUTH_SECRET")
REFRESH_ENC_FILE = os.getenv("REFRESH_ENC")
REFRESH_DEC_FILE = os.getenv("REFRESH_DEC")
REFRESH_SECRET = os.getenv("REFRESH_SECRET")

AUTH_EXPIRATION = timedelta(minutes=int(os.getenv("AUTH_EXPIRATION_MINUTE") or "12"))
REFRESH_EXPIRATION = timedelta(minutes=int(os.getenv("REFRESH_EXPIRATION_MINUTE") or "1440"))


class AuthModel:
    def __init__(
        self,
        auth_enc=None,
        auth_dec=None,
        refresh_enc=None,
        refresh_dec=None,
        auth_secret=AUTH_SECRET,
        refresh_secret=REFRESH_SECRET,
        auth_expiration=AUTH_EXPIRATION,
        refresh_expiration=REFRESH_EXPIRATION
    ):
        if (not auth_enc) != (not auth_dec):
            raise Exception("Please provide both auth_enc and auth_dec or neither")
        if (not refresh_enc) != (not refresh_dec):
            raise Exception("Please provide both refresh_enc and refresh_dec or neither")

        if auth_enc and auth_dec:
            self.set_auth(auth_enc, auth_dec)
        else:
            self.read_auth()
        if refresh_enc and refresh_dec:
            self.set_refresh(refresh_enc, refresh_dec)
        else:
            self.read_refresh()

        self.auth_secret = auth_secret
        self.refresh_secret = refresh_secret
        self.auth_expiration = auth_expiration
        self.refresh_expiration = refresh_expiration

    def read_auth(self):
        with open(AUTH_ENC_FILE, "r") as f:
            auth_enc = f.read()
        with open(AUTH_DEC_FILE, "r") as f:
            auth_dec = f.read()
        self.set_auth(auth_enc, auth_dec)

    def read_refresh(self):
        with open(REFRESH_ENC_FILE, "r") as f:
            refresh_enc = f.read()
        with open(REFRESH_DEC_FILE, "r") as f:
            refresh_dec = f.read()
        self.set_refresh(refresh_enc, refresh_dec)

    def set_auth(self, auth_enc, auth_dec):
        self.auth_enc, self.auth_dec = auth_enc, auth_dec

    def set_refresh(self, refresh_enc, refresh_dec):
        self.refresh_enc, self.refresh_dec = refresh_enc, refresh_dec


    def encode_auth(self, payload, now=None):
        return encode_jwt(payload, self.auth_enc, self.auth_expiration, now=now)

    def decode_auth(self, token):
        try:
            return decode_jwt(token, self.auth_dec, issuer=self.auth_secret)
        except jwt.ExpiredSignatureError:
            raise TAuthError(TAuthErrorCode.AUTH_TOKEN_EXPIRED)
        except (jwt.InvalidIssuerError, jwt.InvalidAudienceError, jwt.DecodeError):
            raise TAuthError(TAuthErrorCode.AUTH_TOKEN_INVALID)

    def encode_refresh(self, payload, now=None):
        return encode_jwt(payload, self.refresh_enc, self.refresh_expiration, now=now)

    def decode_refresh(self, token, auth_secret_2):
        try:
            return decode_jwt(token, self.refresh_dec, issuer=self.refresh_secret, audience=auth_secret_2)
        except jwt.ExpiredSignatureError:
            raise TLoginError(TLoginErrorCode.REFRESH_TOKEN_EXPIRED)
        except (jwt.InvalidIssuerError, jwt.InvalidAudienceError, jwt.DecodeError):
            raise TLoginError(TLoginErrorCode.REFRESH_TOKEN_INVALID)

    def make_pair(self, auth_payload=None, now=None, user=None):
        if not (auth_payload or user):
            raise Exception("Please provide payload or user")
        if not auth_payload:
            auth_payload = {
                'user_id': user.id,
                'role': user.role
            }
        auth_payload['iss'] = self.auth_secret

        now = now or datetime.utcnow()
        user_id = auth_payload['user_id']
        user_id_str = str(user_id)
        now_ts = str(now.timestamp())

        auth_payload['auth_secret_2'] = md5(user_id_str + 'uauth' + now_ts + self.auth_secret)
        auth_token = self.encode_auth(auth_payload, now=now)

        refresh_secret_2 = md5(user_id_str + 'urefresh' + now_ts + self.refresh_secret)
        user_model = get_model("user")
        with DBSession() as session:
            user = user_model._get_user(session, user_id)
            user.set_refresh_secret_2(refresh_secret_2)
            session.commit()

        refresh_payload = {
            'iss': self.refresh_secret,
            'aud': auth_payload['auth_secret_2'],
            'refresh_secret_2': refresh_secret_2
        }
        refresh_token = self.encode_refresh(refresh_payload, now=now)
        return auth_token, refresh_token


    def login(self, username, password):
        if not username:
            raise TLoginError(TLoginErrorCode.USERNAME_EMPTY)
        if not password:
            raise TLoginError(TLoginErrorCode.PASSWORD_EMPTY)

        with DBSession() as session:
            user = session.query(DBUser).filter((DBUser.username == username) | (DBUser.email == username)).scalar()
            if not (user and user.verify_password(password)):
                raise TLoginError(TLoginErrorCode.USERNAME_PASSWORD_SALAH)
            if not user.enabled:
                raise TLoginError(TLoginErrorCode.USER_DISABLED)

        return self.make_pair(user=user)

    def refresh_auth(self, auth_token, refresh_token):
        auth_payload = self.decode_auth(auth_token)
        refresh_payload = self.decode_refresh(refresh_token, auth_payload['auth_secret_2'])
        
        user_model = get_model("user")
        user = user_model.get_user(auth_payload['user_id'])
        if not (user and user.enabled and user.refresh_secret_2 and user.refresh_secret_2 == refresh_payload['refresh_secret_2']):
            raise TLoginError(TLoginErrorCode.REFRESH_TOKEN_EXPIRED)

        auth_token = self.encode_auth(auth_payload)
        return auth_token

    def require_role(self, auth_token, role):
        auth_payload = self.decode_auth(auth_token)
        if not (role in T_USER_ROLE_DOUBLES and auth_payload['role'] in T_USER_ROLE_DOUBLES[role]):
            raise TAuthError(TAuthErrorCode.ROLE_INVALID)
        return auth_payload