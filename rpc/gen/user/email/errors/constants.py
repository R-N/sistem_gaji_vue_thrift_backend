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
from .ttypes import *
T_USER_EMAIL_ERROR_STR = {
        6: "Token ganti email kadaluarsa",
        5: "Token ganti email invalid",
        4: "Token verifikasi email kadaluarsa",
        3: "Token verifikasi email invalid",
        2: "Token reset password kadaluarsa",
        1: "Token reset password invalid",
}
