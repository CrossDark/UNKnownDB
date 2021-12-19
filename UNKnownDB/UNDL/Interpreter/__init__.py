"""
Interpreter
import UNDL
"""
__author__ = 'CleverCreator'
import re


class Interpret:
    def __init__(self, code_list):
        self.Code = code_list
        self.Guide = []
        self.Form = []
        self.Info = []
        self.GuideDict = {}
        self.FormDict = {}
        self.InfoDict = {}
        on_tab_block = False
        on_key_block = None
        for code_str in code_list:
            code = re.findall('( {4})?(.+)(?!Guide|Form|Info|Name|IP|Port|Head|Body):(.+)?', code_str)
            if code[0][0] == '':
                on_key_block = eval('self.' + str(code[0][1]))
                on_tab_block = True
            elif on_tab_block:
                on_key_block.append(code[0][2])

    def change(self, search, changes):
        re.sub(search, changes, self.Code)

    def refactoring(self):
        return self.Code.remove([])

    def dictionary(self):
        on_tab_block = False
        on_key_block = None
        for code_str in self.Code:
            code = re.findall('( {4})?(.+)(?!Guide|Form|Info|Name|IP|Port|Head):(.+)?', code_str)
            if code[0][0] == '':
                on_key_block = eval('self.' + str(code[0][1]) + 'Dict')
                on_tab_block = True
            elif on_tab_block:
                on_key_block[code[0][1]] = code[0][2]
        return self.GuideDict, self.FormDict, self.InfoDict


class Form:
    def __init__(self, form: [], dictionary: {}):
        self.Form = [form_str.split(' ') for form_str in form]
        self.Dict = dictionary
        self.Type = []

    def search(self, key_word):
        pass

    def find(self, *index, **name):
        pass

    def type(self):
        self.Type = [type(key) for key in self.Form[1]]
        return self.Type
