"""
Interpreter
import UNDL
"""
import re


class Interpreter:
    def __init__(self, undl):
        self.undl = undl
        self.Name = None
        with open(self.undl) as code:
            self.code = code.readlines()

    def name(self):
        for code in self.code:
            self.Name = re.match("Name:(.*)", code)
            print(self.Name)
            if self.Name:
                break
            else:
                self.Name = None
        print(self.Name)

    def interpret(self):
        for code in self.code:
            re.findall(re.compile("r[Name](.*?)"), code)
