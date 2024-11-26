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


class TJobLevel(object):
    """
    Attributes:
     - id
     - enabled
     - name
     - gaji_pokok
     - tunjangan_jabatan
     - upah_lembur_1
     - upah_lembur_2
     - upah_lembur_3

    """


    def __init__(self, id=None, enabled=None, name=None, gaji_pokok=None, tunjangan_jabatan=None, upah_lembur_1=None, upah_lembur_2=None, upah_lembur_3=None,):
        self.id = id
        self.enabled = enabled
        self.name = name
        self.gaji_pokok = gaji_pokok
        self.tunjangan_jabatan = tunjangan_jabatan
        self.upah_lembur_1 = upah_lembur_1
        self.upah_lembur_2 = upah_lembur_2
        self.upah_lembur_3 = upah_lembur_3

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
                if ftype == TType.I32:
                    self.id = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.BOOL:
                    self.enabled = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.name = iprot.readString().decode('utf-8', errors='replace') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.gaji_pokok = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.tunjangan_jabatan = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I32:
                    self.upah_lembur_1 = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I32:
                    self.upah_lembur_2 = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.I32:
                    self.upah_lembur_3 = iprot.readI32()
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
        oprot.writeStructBegin('TJobLevel')
        if self.id is not None:
            oprot.writeFieldBegin('id', TType.I32, 1)
            oprot.writeI32(self.id)
            oprot.writeFieldEnd()
        if self.enabled is not None:
            oprot.writeFieldBegin('enabled', TType.BOOL, 2)
            oprot.writeBool(self.enabled)
            oprot.writeFieldEnd()
        if self.name is not None:
            oprot.writeFieldBegin('name', TType.STRING, 3)
            oprot.writeString(self.name.encode('utf-8') if sys.version_info[0] == 2 else self.name)
            oprot.writeFieldEnd()
        if self.gaji_pokok is not None:
            oprot.writeFieldBegin('gaji_pokok', TType.I32, 4)
            oprot.writeI32(self.gaji_pokok)
            oprot.writeFieldEnd()
        if self.tunjangan_jabatan is not None:
            oprot.writeFieldBegin('tunjangan_jabatan', TType.I32, 5)
            oprot.writeI32(self.tunjangan_jabatan)
            oprot.writeFieldEnd()
        if self.upah_lembur_1 is not None:
            oprot.writeFieldBegin('upah_lembur_1', TType.I32, 6)
            oprot.writeI32(self.upah_lembur_1)
            oprot.writeFieldEnd()
        if self.upah_lembur_2 is not None:
            oprot.writeFieldBegin('upah_lembur_2', TType.I32, 7)
            oprot.writeI32(self.upah_lembur_2)
            oprot.writeFieldEnd()
        if self.upah_lembur_3 is not None:
            oprot.writeFieldBegin('upah_lembur_3', TType.I32, 8)
            oprot.writeI32(self.upah_lembur_3)
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


class TJobLevelForm(object):
    """
    Attributes:
     - name
     - gaji_pokok
     - tunjangan_jabatan
     - upah_lembur_1
     - upah_lembur_2
     - upah_lembur_3

    """


    def __init__(self, name=None, gaji_pokok=None, tunjangan_jabatan=None, upah_lembur_1=None, upah_lembur_2=None, upah_lembur_3=None,):
        self.name = name
        self.gaji_pokok = gaji_pokok
        self.tunjangan_jabatan = tunjangan_jabatan
        self.upah_lembur_1 = upah_lembur_1
        self.upah_lembur_2 = upah_lembur_2
        self.upah_lembur_3 = upah_lembur_3

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
                    self.name = iprot.readString().decode('utf-8', errors='replace') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.gaji_pokok = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.tunjangan_jabatan = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.upah_lembur_1 = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.upah_lembur_2 = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I32:
                    self.upah_lembur_3 = iprot.readI32()
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
        oprot.writeStructBegin('TJobLevelForm')
        if self.name is not None:
            oprot.writeFieldBegin('name', TType.STRING, 1)
            oprot.writeString(self.name.encode('utf-8') if sys.version_info[0] == 2 else self.name)
            oprot.writeFieldEnd()
        if self.gaji_pokok is not None:
            oprot.writeFieldBegin('gaji_pokok', TType.I32, 2)
            oprot.writeI32(self.gaji_pokok)
            oprot.writeFieldEnd()
        if self.tunjangan_jabatan is not None:
            oprot.writeFieldBegin('tunjangan_jabatan', TType.I32, 3)
            oprot.writeI32(self.tunjangan_jabatan)
            oprot.writeFieldEnd()
        if self.upah_lembur_1 is not None:
            oprot.writeFieldBegin('upah_lembur_1', TType.I32, 4)
            oprot.writeI32(self.upah_lembur_1)
            oprot.writeFieldEnd()
        if self.upah_lembur_2 is not None:
            oprot.writeFieldBegin('upah_lembur_2', TType.I32, 5)
            oprot.writeI32(self.upah_lembur_2)
            oprot.writeFieldEnd()
        if self.upah_lembur_3 is not None:
            oprot.writeFieldBegin('upah_lembur_3', TType.I32, 6)
            oprot.writeI32(self.upah_lembur_3)
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


class TJobLevelQuery(object):
    """
    Attributes:
     - limit
     - offset
     - enabled

    """


    def __init__(self, limit=None, offset=None, enabled=None,):
        self.limit = limit
        self.offset = offset
        self.enabled = enabled

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
                if ftype == TType.I32:
                    self.limit = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.offset = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.BOOL:
                    self.enabled = iprot.readBool()
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
        oprot.writeStructBegin('TJobLevelQuery')
        if self.limit is not None:
            oprot.writeFieldBegin('limit', TType.I32, 1)
            oprot.writeI32(self.limit)
            oprot.writeFieldEnd()
        if self.offset is not None:
            oprot.writeFieldBegin('offset', TType.I32, 2)
            oprot.writeI32(self.offset)
            oprot.writeFieldEnd()
        if self.enabled is not None:
            oprot.writeFieldBegin('enabled', TType.BOOL, 3)
            oprot.writeBool(self.enabled)
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
all_structs.append(TJobLevel)
TJobLevel.thrift_spec = (
    None,  # 0
    (1, TType.I32, 'id', None, None, ),  # 1
    (2, TType.BOOL, 'enabled', None, None, ),  # 2
    (3, TType.STRING, 'name', 'UTF8', None, ),  # 3
    (4, TType.I32, 'gaji_pokok', None, None, ),  # 4
    (5, TType.I32, 'tunjangan_jabatan', None, None, ),  # 5
    (6, TType.I32, 'upah_lembur_1', None, None, ),  # 6
    (7, TType.I32, 'upah_lembur_2', None, None, ),  # 7
    (8, TType.I32, 'upah_lembur_3', None, None, ),  # 8
)
all_structs.append(TJobLevelForm)
TJobLevelForm.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'name', 'UTF8', None, ),  # 1
    (2, TType.I32, 'gaji_pokok', None, None, ),  # 2
    (3, TType.I32, 'tunjangan_jabatan', None, None, ),  # 3
    (4, TType.I32, 'upah_lembur_1', None, None, ),  # 4
    (5, TType.I32, 'upah_lembur_2', None, None, ),  # 5
    (6, TType.I32, 'upah_lembur_3', None, None, ),  # 6
)
all_structs.append(TJobLevelQuery)
TJobLevelQuery.thrift_spec = (
    None,  # 0
    (1, TType.I32, 'limit', None, None, ),  # 1
    (2, TType.I32, 'offset', None, None, ),  # 2
    (3, TType.BOOL, 'enabled', None, None, ),  # 3
)
fix_spec(all_structs)
del all_structs
