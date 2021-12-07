"""
Interpreter
import UNDL
"""
import re


class Interpreter:
    def __init__(self, undl):
        self.undl = undl
        with open(self.undl) as code:
            self.code = code.read()

    def name(self):
        if re.compile('Name;(.+)\n'):
            print(10)
        else:
            print(1)
