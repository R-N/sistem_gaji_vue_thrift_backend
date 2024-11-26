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

from thrift.transport import TTransport
all_structs = []


class TUserEmailErrorCode(object):
    ZERO = 0
    RESET_PASSWORD_TOKEN_INVALID = 1
    RESET_PASSWORD_TOKEN_EXPIRED = 2
    EMAIL_VERIFICATION_TOKEN_INVALID = 3
    EMAIL_VERIFICATION_TOKEN_EXPIRED = 4
    EMAIL_CHANGE_TOKEN_INVALID = 5
    EMAIL_CHANGE_TOKEN_EXPIRED = 6

    _VALUES_TO_NAMES = {
        0: "ZERO",
        1: "RESET_PASSWORD_TOKEN_INVALID",
        2: "RESET_PASSWORD_TOKEN_EXPIRED",
        3: "EMAIL_VERIFICATION_TOKEN_INVALID",
        4: "EMAIL_VERIFICATION_TOKEN_EXPIRED",
        5: "EMAIL_CHANGE_TOKEN_INVALID",
        6: "EMAIL_CHANGE_TOKEN_EXPIRED",
    }

    _NAMES_TO_VALUES = {
        "ZERO": 0,
        "RESET_PASSWORD_TOKEN_INVALID": 1,
        "RESET_PASSWORD_TOKEN_EXPIRED": 2,
        "EMAIL_VERIFICATION_TOKEN_INVALID": 3,
        "EMAIL_VERIFICATION_TOKEN_EXPIRED": 4,
        "EMAIL_CHANGE_TOKEN_INVALID": 5,
        "EMAIL_CHANGE_TOKEN_EXPIRED": 6,
    }


class TUserEmailError(TException):
    """
    Attributes:
     - code

    """


    def __init__(self, code=None,):
        super(TUserEmailError, self).__setattr__('code', code)

    def __setattr__(self, *args):
        raise TypeError("can't modify immutable instance")

    def __delattr__(self, *args):
        raise TypeError("can't modify immutable instance")

    def __hash__(self):
        return hash(self.__class__) ^ hash((self.code, ))

    @classmethod
    def read(cls, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and cls.thrift_spec is not None:
            return iprot._fast_decode(None, iprot, [cls, cls.thrift_spec])
        iprot.readStructBegin()
        code = None
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    code = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()
        return cls(
            code=code,
        )

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('TUserEmailError')
        if self.code is not None:
            oprot.writeFieldBegin('code', TType.I32, 1)
            oprot.writeI32(self.code)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __str__(self):
        return repr(self)

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(TUserEmailError)
TUserEmailError.thrift_spec = (
    None,  # 0
    (1, TType.I32, 'code', None, None, ),  # 1
)
fix_spec(all_structs)
del all_structs