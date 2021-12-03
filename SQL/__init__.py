"""A SQL"""
import os


class LocalDB:
    def __init__(self):
        self.path = ''
        self.sql = None
        self.sqlData = None

    def create(self, path='./.Clever.undb'):
        self.path = path
        base_path = ['.OBJECT.undb', '.MAPPING.undb']
        try:
            os.mkdir(self.path)
            os.chdir(self.path)
            for i in base_path:
                os.mkdir('./' + i)
            os.mknod('./Guide.undb')
        except FileExistsError:
            pass

    def __enter__(self, path: str):
        self.path = path
        os.chdir(self.path)
        with open('./Guide.undb.info', 'rb') as self.sql:
            self.sqlData = self.sql.read()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.sql = None
        self.sqlData = None


class WebDB:
    def __init__(self):
        self.form = None
