"""
Light DataBase
"""
import os
import re


class File:
    def __init__(self, path, name='light'):
        self.path = path + '.unl'
        self.name = name

    def __enter__(self, ):
        if not os.path.isfile(self.path):
            open_ = open(self.path, 'wb')
            open_.write(bytes('' + self.name + '', 'UTF-8'))
            open_.close()
        self.DB = open(self.path, 'rb+')
        self.DB.readable()
        self.DB.writable()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.DB.close()
        self.DB = open(self.path, 'r')
        dbb = self.DB.read()
        self.DB.close()
        print(dbb)
        with open(self.path, 'w') as new:
            new.write(dbb.replace(chr(0), ''))

    def __add__(self, other):
        write = re.findall('(.+):(.+)', other)
        self.DB.seek(0, 2)
        self.DB.write(bytes('' + write[0][0] + '' + write[0][1] + '', 'utf-8'))
        return self

    def __sub__(self, other):
        """-"""
        write = re.findall('(.+):(.+)', other)
        change = '' + write[0][0] + '' + write[0][1] + ''
        change_list = [(m.group(), m.span()) for m in re.finditer(change, str(self.DB.read(), 'utf-8'))]
        self.DB.seek(change_list[0][1][0])
        self.DB.write(bytes(chr(0)*(change_list[0][1][1] - change_list[0][1][0]), 'utf-8'))
        return self

    def __setitem__(self, key, value):
        """[]"""
        if '' + key + '' in str(self.DB.read(), 'utf-8'):
            print(9999)
            change_list = [(m.group(), m.span()) for m in re.finditer('' + key + '(.+)', str(self.DB.read(), 'utf-8'))]
            self.DB.seek(change_list[0][1][0])
            self.DB.write(bytes('' + key + '' + value + '', 'utf-8'))
        else:
            self.DB.seek(0, 2)
            self.DB.write(bytes('' + key+ '' + value + '', 'utf-8'))



