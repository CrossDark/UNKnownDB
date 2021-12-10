"""
Interpreter
import UNDL
"""
import re


class Interpreter:
    def __init__(self, undl):
        self.undl = undl
        self.Name = None
        self.IP = None
        self.Port = None
        with open(self.undl) as code:
            self.code = code.readlines()

    def name(self):
        for code in self.code:
            self.Name = re.findall('^Name:(.+?)\n', code)
            if self.Name:
                break
            else:
                self.Name = None
        return self.Name

    def ip(self):
        for code in self.code:
            self.IP = re.findall('^IP:(.+?)\n', code)
            if self.IP:
                break
        return self.IP

    def port(self):
        for code in self.code:
            self.Port = re.findall('^Port:(.+?)\n', code)
            if self.Port:
                break
        return self.Port
