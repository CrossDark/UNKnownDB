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


class Interpret:
    def __init__(self, undl):
        with open(undl) as self.undl:
            self.code = self.undl.readlines()
        find = (re.findall('^(Guide|Form|Relation):$(.+?)', code) for code in self.code)
        print(str(find))


class Guide(Base):
    def name(self):
        for code in self.Code:
            self.Name = re.findall('^Name:$(.+?)', code)
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
    def base(self):
        form = False
        for code in self.Code:
            if not form:
                self.Form = re.findall('^Form:(.+?)\n', code)
            if self.Form:
                form = True
            if form:
                self.FormIndex.append(re.findall('^[ ]{4}(.+?)\n', code))
        try:
            self.FormIndex.remove([])
        except ValueError:
            pass
        return self.FormIndex

    def create(self):
        form = {}
        for form_data in self.FormIndex:
            form_str = re.findall('^(.+?):(.+?)$', form_data[0])
            form_list = list(form_str[0])
            form[form_list[0]] = form_list[1]
        self.FormDict = form
        self.FormApply[self.Form[0]] = form
        return self.FormApply

    def change(self):
        pass

    def index(self):
        # key = self.FormApply[self.Form]['Head']
        # key_list = key.split(' ')
        keys = [[name, [[n, t.split] for n, t in things]] for name, things in self.FormApply.items()]
        return keys
