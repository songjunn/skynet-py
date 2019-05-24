# coding: utf-8
import struct
import binascii
import socket

class Protocol(object):
    def __init__(self):
        self._size = 0
        self._type = 0
        self._data = ""

    def package(self, type, data):
        self._type = type
        self._data = data
        self._size = 4 + len(data)
        s = struct.Struct('ii' + str(len(data)) + 's')
        v = (self._size, self._type, self._data)
        return s.pack(*v)

    def unpackage(self, data):
        # get header
        if len(data) < 4:
            return False
        self._size, = struct.unpack('i', data[0:4])
        # get body
        if len(data) - 4 < self._size:
            return False
        self._type, self._data, = struct.unpack('i' +
            str(self._size - 4) + 's', data[4:self._size+4])
        return True

    def type(self):
        return self._type

    def size(self):
        return self._size

    def data(self):
        return self._data
