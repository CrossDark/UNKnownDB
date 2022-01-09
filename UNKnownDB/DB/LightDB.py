"""
Light DataBase
"""
import os
import re


class Data:
    def __init__(self, path, name='light'):
        self.path = path + '.unl'
        self.name = name
        self.path_list = []
        self.split = None
        self.split_index = 0

    def __enter__(self):
        try:
            self.__find()
        except FileNotFoundError:
            open_ = open(self.path, 'wb')
            open_.write(bytes('' + self.name + '00', 'UTF-8'))
            open_.close()
        self.DB = open(self.path, 'rb+')
        self.DB.seek(0, 0)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.DB.close()

    def __add__(self, other):
        """+"""
        write = re.findall('(.+):(.+)', other)
        self.DB.seek(0, 2)
        self.DB.write(bytes('' + write[0][0] + '' + write[0][1] + '', 'utf-8'))
        self.DB.seek(0, 0)
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
        if '' + key + '' in str(self.DB.read(), 'utf-8'):
            change_list = [(m.group(), m.span()) for m in re.finditer('' + key + '.+?', str(self.DB.read(), 'utf-8'))]
            self.DB.seek(change_list[0][1][0], 0)
            self.DB.truncate(change_list[0][1][0])
            self.DB.seek(0, 2)
            self.DB.write(bytes('' + key + '' + value + '', 'utf-8'))
        else:
            self.DB.seek(0, 2)
            self.DB.write(bytes('' + key+ '' + value + '', 'utf-8'))
        self.DB.seek(0, 0)

    def __getitem__(self, item):
        """[]"""
        self.DB.seek(0, 0)
        returns =  [(m.group(), m.span()) for m in re.finditer('' + item + '.+?', str(self.DB.read(), 'utf-8'))]
        return [re.sub('|||' + item, '', i[0]) for i in returns]

    def __delitem__(self, key):
        delete = re.findall('' + key + '(.+?)', str(self.DB.read(), 'utf-8'))
        self.__sub__(key + ':' + delete[0])

    def __str__(self):
        return re.sub('[]',' ', str(self.DB.read(), 'utf-8'))

    def __repr__(self):
        return self.__all()

    def __len__(self):
        return len([m.group() for m in self.__all()])

    def __int__(self):
        return 1

    def __missing__(self, key):
        return key + 'not find'

    def __iter__(self):
        self.__split()
        return self

    def __next__(self):
        self.split_index += 1
        try:
            return self.split[self.split_index - 1]
        except IndexError:
            raise StopIteration

    def __split(self):
        self.split = re.split('[]', str(self.DB.read(), 'utf-8'))
        self.split.remove('light')
        self.split = [i for i in self.split if i != '']

    def __all(self):
        self.DB.seek(0 ,0)
        for m in re.finditer('.+?.+?', str(self.DB.read(), 'utf-8')):
            yield m

    def __find(self, path=os.path.expanduser('~')):
        for i in os.listdir(path):
            path_file = os.path.join(path, i)
            if os.path.isfile(path_file):
                if os.path.splitext(path_file)[1] == '.unl':
                    with open(path_file, 'r') as check:
                        if re.match('.+?' + self.name + '.+?', check.read()):
                            self.path = path_file
            elif os.path.basename(path_file)[0] == '.':
                pass
            else:
                self.__find(path_file)


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
