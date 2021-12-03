"""A SQL"""


class SQL:
    def __init__(self):
        self.path = ''
        self.sql = None
        self.sqlData = None

    def create(self, path):
        self.path = path
        with open(path, 'wb') as self.sql:
            self.sql.write(self.path)

    def connect(self, path):
        self.path = path
        with open(path, 'rb') as self.sql:
            self.sqlData = self.sql.read()

    def __enter__(self, path):
        assert path == str
        self.path = path
        with open(path, 'rb') as self.sql:
            self.sqlData = self.sql.read()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.sql = None
        self.sqlData = None


class Form:
    def __init__(self):
        self.form = None
