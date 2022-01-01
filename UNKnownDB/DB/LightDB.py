"""
Light DataBase
"""
import os.path


class File:
    def __init__(self, path, name='light'):
        self.path = path + '.unl'
        self.name = name

    def __enter__(self,):
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

    def __add__(self, other):
        self.DB.seek(0)
        self.DB.write(bytes(other, 'utf-8'))
        return self
