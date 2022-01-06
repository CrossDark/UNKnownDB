"""
Light DataBase
"""
import os
import re


class Data:
    def __init__(self, path, name='light'):
        self.path = path + '.unl'
        self.name = name

    def __enter__(self, ):
        if not os.path.isfile(self.path):
            open_ = open(self.path, 'wb')
            open_.write(bytes('' + self.name + '', 'UTF-8'))
            open_.close()
        self.DB = open(self.path, 'rb+')
        self.read = self.DB.read()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.DB.close()
        with open(self.path, 'r') as db:
            dbb = db.read()
        with open(self.path, 'w') as new:
            new.write(dbb.replace(chr(0), ''))

    def __add__(self, other):
        """+"""
        write = re.findall('(.+):(.+)', other)
        self.DB.seek(0, 2)
        self.DB.write(bytes('' + write[0][0] + '' + write[0][1] + '', 'utf-8'))
        return self

    def __sub__(self, other):
        """-"""
        self.DB.seek(0, 0)
        changing = str(self.DB.read(), 'utf-8')
        write = re.findall('(.+):(.+)', other)
        change = '' + write[0][0] + '' + write[0][1] + ''
        change_list = [(m.group(), m.span()) for m in re.finditer(change, changing)]
        self.DB.seek(change_list[0][1][0], 0)
        self.DB.truncate(change_list[0][1][0])
        self.DB.seek(0, 2)
        self.DB.write(bytes(changing[change_list[0][1][1]:], 'utf-8'))
        return self

    def __setitem__(self, key, value):
        """[] = ?"""
        self.DB.seek(0, 0)
        if '' + key + '' in str(self.read, 'utf-8'):
            change_list = [(m.group(), m.span()) for m in re.finditer('' + key + '.+?', str(self.DB.read(), 'utf-8'))]
            self.DB.seek(change_list[0][1][0], 0)
            self.DB.truncate(change_list[0][1][0])
            self.DB.seek(0, 2)
            self.DB.write(bytes('' + key + '' + value + '', 'utf-8'))
        else:
            self.DB.seek(0, 2)
            self.DB.write(bytes('' + key+ '' + value + '', 'utf-8'))

    def __getitem__(self, item):
        """[]"""
        self.DB.seek(0, 0)
        returns =  [(m.group(), m.span()) for m in re.finditer('' + item + '.+?', str(self.DB.read(), 'utf-8'))]
        return [re.sub('|||' + item, '', i[0]) for i in returns]

    def all(self):
        for m in re.finditer('.+?.+?', str(self.read, 'utf-8')):
            return re.sub('|||', '',  m.group(),), m.span()

    def find(self):
        pass


class File(Data):
    def __add__(self, other):
        """+"""
        write = re.findall('(.+):(.+)', other)
        self.DB.seek(0, 2)
        if os.path.isfile(write[0][1]) is True:
            split = os.path.split(write[0][1])
            os.rename(write[0][1], str(hash(split[0])) + '.unf' + split[1])
            self.DB.write(bytes('' + write[0][0] + '' + os.path.abspath(write[0][1]) + '', 'utf-8'))
        else:
            return False
        return self
