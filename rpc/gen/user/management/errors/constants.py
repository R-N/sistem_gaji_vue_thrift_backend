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
T_USER_MANAGEMENT_ERROR_STR = {
        1: "Tidak dapat menghapus akun yang telah terverifikasi",
        2: "Anda tidak berhak melakukan ini pada user dengan peran lebih tinggi daripada Anda",
        3: "Anda tidak berhak menentukan role yang lebih tinggi daripada Anda",
        4: "Password kosong",
}
