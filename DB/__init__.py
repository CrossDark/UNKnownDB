"""A DB"""
import os
import shutil


class LocalDB:
    def __init__(self):
        self.path = ''
        self.db = None
        self.dbData = None

    def create(self, path='./.Clever.undb'):
        self.path = path
        base_path = ['.OBJECT.undb', '.MAPPING.undb']
        try:
            os.mkdir(self.path)
            os.chdir(self.path)
            for i in base_path:
                os.mkdir('./' + i)
            os.mknod('./Guide.undb')
            with open('./Guide.undb', 'w') as self.dbData:
                self.dbData.write('po')
        except FileExistsError:
            self.delete_all(self.path)

    def __enter__(self, path: str):
        self.path = path
        os.chdir(self.path)
        with open('./Guide.undb.info', 'rb') as self.sql:
            self.sqlData = self.sql.read()

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


class WebDB:
    def __init__(self):
        self.form = None
