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
T_EMAIL_ERROR_STR = {
        3: "Email invalid",
        4: "Email tidak ditemukan",
        5: "Gagal mengirim email",
        2: "Email token kadaluarsa",
        1: "Email token invalid",
}