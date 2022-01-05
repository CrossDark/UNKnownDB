"""
A DSL
"""


class Main:
    def __init__(self, doc: str):
        super(Main, self).__init__()
        self.file = doc
        self.file.split('~')
