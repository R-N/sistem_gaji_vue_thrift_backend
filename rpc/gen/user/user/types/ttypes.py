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


class TUserRole(object):
    ZERO = 0
    KARYAWAN = 1
    ADMIN_BIASA = 2
    ADMIN_UTAMA = 3
    ADMIN_AKUN = 4
    PENGAWAS = 5
    SUPER_ADMIN = 6

    _VALUES_TO_NAMES = {
        0: "ZERO",
        1: "KARYAWAN",
        2: "ADMIN_BIASA",
        3: "ADMIN_UTAMA",
        4: "ADMIN_AKUN",
        5: "PENGAWAS",
        6: "SUPER_ADMIN",
    }

    _NAMES_TO_VALUES = {
        "ZERO": 0,
        "KARYAWAN": 1,
        "ADMIN_BIASA": 2,
        "ADMIN_UTAMA": 3,
        "ADMIN_AKUN": 4,
        "PENGAWAS": 5,
        "SUPER_ADMIN": 6,
    }
fix_spec(all_structs)
del all_structs