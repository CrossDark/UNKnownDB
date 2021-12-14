"""
Interpreter
import UNDL
"""
__author__ = 'CleverCreator'
import re


class Base:

    def __init__(self, undl):
        self.Undl = undl
        self.Name = None
        self.IP = None
        self.Port = None
        self.Form = None
        self.FormIndex = []
        self.FormHead = []
        self.FormApply = {}
        self.FormDict = {}
        with open(self.Undl) as code:
            self.Code = code.readlines()


class Guide(Base):
    def name(self):
        for code in self.Code:
            self.Name = re.findall('^Name:(.+?)\n', code)
            if self.Name:
                break
            else:
                self.Name = None
        return self.Name

    def ip(self):
        for code in self.Code:
            self.IP = re.findall('^IP:(.+?)\n', code)
            if self.IP:
                break
        return self.IP

    def port(self):
        for code in self.Code:
            self.Port = re.findall('^Port:(.+?)\n', code)
            if self.Port:
                break
        return self.Port

    def start(self):
        self.name()
        self.ip()
        self.port()
        return [self.Name, self.IP, self.Port]


class Form(Base):
    def form(self):
        form = False
        for code in self.Code:
            if not form:
                self.Form = re.findall('^Form:(.+?)\n', code)
            if self.Form:
                form = True
            if form:
                self.FormIndex.append(re.findall('^[ ]{4}(.+?)\n', code))
        self.FormIndex.remove([])
        return self.FormIndex

    def create_form(self):
        form = {}
        for form_data in self.FormIndex:
            form_str = re.findall('^(.+?):(.+?)$', form_data[0])
            form_list = list(form_str[0])
            form[form_list[0]] = form_list[1]
        self.FormDict = form
        self.FormApply[self.Form[0]] = form
        return self.FormApply
