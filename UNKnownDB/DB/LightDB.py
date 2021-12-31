"""
Light DataBase
"""
import os.path


class File:
    def __init__(self, path):
        self.path = path

    def __enter__(self,):
        if os.path.isfile(self.path):
            self.DB = open(self.path, 'r+')
        else:
            open(self.path, 'x')
        self.DB.readable()
        self.DB.writable()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.DB.close()

    def __add__(self, other):
        self.DB.seek(10)
        self.DB.write(other)
        return self
