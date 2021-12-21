"""A DB"""
import os
import shutil
import sqlite3
import UNKnownDB.UNDL.Interpreter


class LocalDB:
    def __init__(self, path):
        self.path = path
        self.db = None
        self.dbData = None

    def create(self):
        base_path = ['.OBJECT.unp', '.MAPPING.unp']
        try:
            os.mkdir(self.path)
            os.chdir(self.path)
            for i in base_path:
                os.mkdir('./' + i)
            os.mknod('./Guide.undl')
            with open('./Guide.undl', 'w') as self.dbData:
                split = os.path.split(self.path)
                split_text = os.path.splitext(split[1])
                self.dbData.write(
                    'Guide:\n'
                    '    Name:' + split_text[0].removesuffix('.') + '\n'
                    '    IP: <None>\n'
                    '    Port:4466 \n'
                    'Form:try\n'
                    '    Head:clever creator is clever\n'
                    '    Body:op po oo pp\n'
                                  )
        except FileExistsError:
            self.delete_all(self.path)
            os.rmdir(self.path)

    def __enter__(self):
        return UNKnownDB.UNDL.Interpreter

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.sql = None
        self.sqlData = None

    def delete_all(self, delete_path):
        if not os.listdir(delete_path):
            pass
        else:
            for i in os.listdir(delete_path):
                path_file = os.path.join(delete_path, i)
                if os.path.isfile(path_file):
                    os.remove(path_file)
                else:
                    self.delete_all(path_file)
                    shutil.rmtree(path_file)

    def write(self):
        pass


class WebDB:
    def __init__(self):
        self.form = None


class SQLITE:
    def __init__(self, path, sqlite, table):
        self.connection = sqlite3.connect(sqlite)
        self.cursor = self.connection.cursor()
        self.db = UNKnownDB.UNDL.Interpreter.Interpret(path)
        self.cursor.execute('create table ' + table + self.db.Form[0])
        self.cursor.close()
        self.connection.commit()
