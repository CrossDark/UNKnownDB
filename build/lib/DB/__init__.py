"""A DB"""
import os
import shutil


class LocalDB:
    def __init__(self):
        self.path = ''
        self.db = None
        self.dbData = None

    def create(self, path='./.Clever.unp'):
        self.path = path
        base_path = ['.OBJECT.unp', '.MAPPING.unp']
        try:
            os.mkdir(self.path)
            os.chdir(self.path)
            for i in base_path:
                os.mkdir('./' + i)
            os.mknod('./Guide.unp')
            with open('./Guide.unp', 'w') as self.dbData:
                split = os.path.split(self.path)
                split_text = os.path.splitext(split[1])
                self.dbData.write(
                    'Name:' + split_text[0] + '\n'
                    'IP: <None>\n'
                    'Port:4466 \n'
                                  )
        except FileExistsError:
            self.delete_all(self.path)
            os.rmdir(self.path)

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