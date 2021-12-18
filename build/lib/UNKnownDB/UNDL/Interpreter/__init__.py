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
        on_tab_block = False
        on_key_block = None
        for code_str in code_list:
            code = re.findall('( {4})?(Guide|Form|Info|Name|IP|Port|Head|Body):(.+)?', code_str)
            if code[0][0] == '':
                on_key_block = eval('self.' + str(code[0][1]))
                on_tab_block = True
            elif on_tab_block:
                on_key_block.append(code[0][2])

    def change(self, search, changes):
        re.sub(search, changes, self.Code)


class Form:
    def __init__(self, form):
        self.Form = form
