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
    def hello_admin_utama(self, auth_token):
        """
        Parameters:
         - auth_token

        """
        pass


class Client(Iface):
    def __init__(self, iprot, oprot=None):
        self._iprot = self._oprot = iprot
        if oprot is not None:
            self._oprot = oprot
        self._seqid = 0

    def hello_admin_utama(self, auth_token):
        """
        Parameters:
         - auth_token

        """
        self.send_hello_admin_utama(auth_token)
        return self.recv_hello_admin_utama()

    def send_hello_admin_utama(self, auth_token):
        self._oprot.writeMessageBegin('hello_admin_utama', TMessageType.CALL, self._seqid)
        args = hello_admin_utama_args()
        args.auth_token = auth_token
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_hello_admin_utama(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = hello_admin_utama_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.auth_error is not None:
            raise result.auth_error
        raise TApplicationException(TApplicationException.MISSING_RESULT, "hello_admin_utama failed: unknown result")


class Processor(Iface, TProcessor):
    def __init__(self, handler):
        self._handler = handler
        self._processMap = {}
        self._processMap["hello_admin_utama"] = Processor.process_hello_admin_utama
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

    def process_hello_admin_utama(self, seqid, iprot, oprot):
        args = hello_admin_utama_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = hello_admin_utama_result()
        try:
            result.success = self._handler.hello_admin_utama(args.auth_token)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except rpc.gen.user.auth.errors.ttypes.TAuthError as auth_error:
            msg_type = TMessageType.REPLY
            result.auth_error = auth_error
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("hello_admin_utama", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

# HELPER FUNCTIONS AND STRUCTURES


class hello_admin_utama_args(object):
    """
    Attributes:
     - auth_token

    """


    def __init__(self, auth_token=None,):
        self.auth_token = auth_token

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
                    self.auth_token = iprot.readString().decode('utf-8', errors='replace') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('hello_admin_utama_args')
        if self.auth_token is not None:
            oprot.writeFieldBegin('auth_token', TType.STRING, 1)
            oprot.writeString(self.auth_token.encode('utf-8') if sys.version_info[0] == 2 else self.auth_token)
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
all_structs.append(hello_admin_utama_args)
hello_admin_utama_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'auth_token', 'UTF8', None, ),  # 1
)


class hello_admin_utama_result(object):
    """
    Attributes:
     - success
     - auth_error

    """


    def __init__(self, success=None, auth_error=None,):
        self.success = success
        self.auth_error = auth_error

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRING:
                    self.success = iprot.readString().decode('utf-8', errors='replace') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.auth_error = rpc.gen.user.auth.errors.ttypes.TAuthError.read(iprot)
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
        oprot.writeStructBegin('hello_admin_utama_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRING, 0)
            oprot.writeString(self.success.encode('utf-8') if sys.version_info[0] == 2 else self.success)
            oprot.writeFieldEnd()
        if self.auth_error is not None:
            oprot.writeFieldBegin('auth_error', TType.STRUCT, 1)
            self.auth_error.write(oprot)
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
all_structs.append(hello_admin_utama_result)
hello_admin_utama_result.thrift_spec = (
    (0, TType.STRING, 'success', 'UTF8', None, ),  # 0
    (1, TType.STRUCT, 'auth_error', [rpc.gen.user.auth.errors.ttypes.TAuthError, None], None, ),  # 1
)
fix_spec(all_structs)
del all_structs