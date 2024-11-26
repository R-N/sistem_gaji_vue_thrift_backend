#
# Autogenerated by Thrift Compiler (0.20.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py:package_prefix=rpc.gen.
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
from thrift.TRecursive import fix_spec

import sys
import logging
from .ttypes import *
from thrift.Thrift import TProcessor
from thrift.transport import TTransport
all_structs = []


class Iface(object):
    def reset_password(self, username):
        """
        Parameters:
         - username

        """
        pass

    def resend_verification(self, username):
        """
        Parameters:
         - username

        """
        pass


class Client(Iface):
    def __init__(self, iprot, oprot=None):
        self._iprot = self._oprot = iprot
        if oprot is not None:
            self._oprot = oprot
        self._seqid = 0

    def reset_password(self, username):
        """
        Parameters:
         - username

        """
        self.send_reset_password(username)
        self.recv_reset_password()

    def send_reset_password(self, username):
        self._oprot.writeMessageBegin('reset_password', TMessageType.CALL, self._seqid)
        args = reset_password_args()
        args.username = username
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_reset_password(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = reset_password_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.login_error is not None:
            raise result.login_error
        if result.user_error is not None:
            raise result.user_error
        if result.email_error is not None:
            raise result.email_error
        if result.user_email_error is not None:
            raise result.user_email_error
        return

    def resend_verification(self, username):
        """
        Parameters:
         - username

        """
        self.send_resend_verification(username)
        self.recv_resend_verification()

    def send_resend_verification(self, username):
        self._oprot.writeMessageBegin('resend_verification', TMessageType.CALL, self._seqid)
        args = resend_verification_args()
        args.username = username
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_resend_verification(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = resend_verification_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.login_error is not None:
            raise result.login_error
        if result.user_error is not None:
            raise result.user_error
        if result.email_error is not None:
            raise result.email_error
        if result.user_email_error is not None:
            raise result.user_email_error
        return


class Processor(Iface, TProcessor):
    def __init__(self, handler):
        self._handler = handler
        self._processMap = {}
        self._processMap["reset_password"] = Processor.process_reset_password
        self._processMap["resend_verification"] = Processor.process_resend_verification
        self._on_message_begin = None

    def on_message_begin(self, func):
        self._on_message_begin = func

    def process(self, iprot, oprot):
        (name, type, seqid) = iprot.readMessageBegin()
        if self._on_message_begin:
            self._on_message_begin(name, type, seqid)
        if name not in self._processMap:
            iprot.skip(TType.STRUCT)
            iprot.readMessageEnd()
            x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % (name))
            oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
            x.write(oprot)
            oprot.writeMessageEnd()
            oprot.trans.flush()
            return
        else:
            self._processMap[name](self, seqid, iprot, oprot)
        return True

    def process_reset_password(self, seqid, iprot, oprot):
        args = reset_password_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = reset_password_result()
        try:
            self._handler.reset_password(args.username)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except rpc.gen.user.auth.errors.ttypes.TLoginError as login_error:
            msg_type = TMessageType.REPLY
            result.login_error = login_error
        except rpc.gen.user.user.errors.ttypes.TUserError as user_error:
            msg_type = TMessageType.REPLY
            result.user_error = user_error
        except rpc.gen.email.errors.ttypes.TEmailError as email_error:
            msg_type = TMessageType.REPLY
            result.email_error = email_error
        except rpc.gen.user.email.errors.ttypes.TUserEmailError as user_email_error:
            msg_type = TMessageType.REPLY
            result.user_email_error = user_email_error
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("reset_password", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_resend_verification(self, seqid, iprot, oprot):
        args = resend_verification_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = resend_verification_result()
        try:
            self._handler.resend_verification(args.username)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except rpc.gen.user.auth.errors.ttypes.TLoginError as login_error:
            msg_type = TMessageType.REPLY
            result.login_error = login_error
        except rpc.gen.user.user.errors.ttypes.TUserError as user_error:
            msg_type = TMessageType.REPLY
            result.user_error = user_error
        except rpc.gen.email.errors.ttypes.TEmailError as email_error:
            msg_type = TMessageType.REPLY
            result.email_error = email_error
        except rpc.gen.user.email.errors.ttypes.TUserEmailError as user_email_error:
            msg_type = TMessageType.REPLY
            result.user_email_error = user_email_error
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("resend_verification", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

# HELPER FUNCTIONS AND STRUCTURES


class reset_password_args(object):
    """
    Attributes:
     - username

    """


    def __init__(self, username=None,):
        self.username = username

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.username = iprot.readString().decode('utf-8', errors='replace') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('reset_password_args')
        if self.username is not None:
            oprot.writeFieldBegin('username', TType.STRING, 1)
            oprot.writeString(self.username.encode('utf-8') if sys.version_info[0] == 2 else self.username)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(reset_password_args)
reset_password_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'username', 'UTF8', None, ),  # 1
)


class reset_password_result(object):
    """
    Attributes:
     - login_error
     - user_error
     - email_error
     - user_email_error

    """


    def __init__(self, login_error=None, user_error=None, email_error=None, user_email_error=None,):
        self.login_error = login_error
        self.user_error = user_error
        self.email_error = email_error
        self.user_email_error = user_email_error

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.login_error = rpc.gen.user.auth.errors.ttypes.TLoginError.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.user_error = rpc.gen.user.user.errors.ttypes.TUserError.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRUCT:
                    self.email_error = rpc.gen.email.errors.ttypes.TEmailError.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRUCT:
                    self.user_email_error = rpc.gen.user.email.errors.ttypes.TUserEmailError.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('reset_password_result')
        if self.login_error is not None:
            oprot.writeFieldBegin('login_error', TType.STRUCT, 1)
            self.login_error.write(oprot)
            oprot.writeFieldEnd()
        if self.user_error is not None:
            oprot.writeFieldBegin('user_error', TType.STRUCT, 2)
            self.user_error.write(oprot)
            oprot.writeFieldEnd()
        if self.email_error is not None:
            oprot.writeFieldBegin('email_error', TType.STRUCT, 3)
            self.email_error.write(oprot)
            oprot.writeFieldEnd()
        if self.user_email_error is not None:
            oprot.writeFieldBegin('user_email_error', TType.STRUCT, 4)
            self.user_email_error.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(reset_password_result)
reset_password_result.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'login_error', [rpc.gen.user.auth.errors.ttypes.TLoginError, None], None, ),  # 1
    (2, TType.STRUCT, 'user_error', [rpc.gen.user.user.errors.ttypes.TUserError, None], None, ),  # 2
    (3, TType.STRUCT, 'email_error', [rpc.gen.email.errors.ttypes.TEmailError, None], None, ),  # 3
    (4, TType.STRUCT, 'user_email_error', [rpc.gen.user.email.errors.ttypes.TUserEmailError, None], None, ),  # 4
)


class resend_verification_args(object):
    """
    Attributes:
     - username

    """


    def __init__(self, username=None,):
        self.username = username

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.username = iprot.readString().decode('utf-8', errors='replace') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('resend_verification_args')
        if self.username is not None:
            oprot.writeFieldBegin('username', TType.STRING, 1)
            oprot.writeString(self.username.encode('utf-8') if sys.version_info[0] == 2 else self.username)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(resend_verification_args)
resend_verification_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'username', 'UTF8', None, ),  # 1
)


class resend_verification_result(object):
    """
    Attributes:
     - login_error
     - user_error
     - email_error
     - user_email_error

    """


    def __init__(self, login_error=None, user_error=None, email_error=None, user_email_error=None,):
        self.login_error = login_error
        self.user_error = user_error
        self.email_error = email_error
        self.user_email_error = user_email_error

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.login_error = rpc.gen.user.auth.errors.ttypes.TLoginError.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.user_error = rpc.gen.user.user.errors.ttypes.TUserError.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRUCT:
                    self.email_error = rpc.gen.email.errors.ttypes.TEmailError.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRUCT:
                    self.user_email_error = rpc.gen.user.email.errors.ttypes.TUserEmailError.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('resend_verification_result')
        if self.login_error is not None:
            oprot.writeFieldBegin('login_error', TType.STRUCT, 1)
            self.login_error.write(oprot)
            oprot.writeFieldEnd()
        if self.user_error is not None:
            oprot.writeFieldBegin('user_error', TType.STRUCT, 2)
            self.user_error.write(oprot)
            oprot.writeFieldEnd()
        if self.email_error is not None:
            oprot.writeFieldBegin('email_error', TType.STRUCT, 3)
            self.email_error.write(oprot)
            oprot.writeFieldEnd()
        if self.user_email_error is not None:
            oprot.writeFieldBegin('user_email_error', TType.STRUCT, 4)
            self.user_email_error.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(resend_verification_result)
resend_verification_result.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'login_error', [rpc.gen.user.auth.errors.ttypes.TLoginError, None], None, ),  # 1
    (2, TType.STRUCT, 'user_error', [rpc.gen.user.user.errors.ttypes.TUserError, None], None, ),  # 2
    (3, TType.STRUCT, 'email_error', [rpc.gen.email.errors.ttypes.TEmailError, None], None, ),  # 3
    (4, TType.STRUCT, 'user_email_error', [rpc.gen.user.email.errors.ttypes.TUserEmailError, None], None, ),  # 4
)
fix_spec(all_structs)
del all_structs
