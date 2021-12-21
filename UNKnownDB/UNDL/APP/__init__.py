"""
thanks:https://blog.csdn.net/weixin_39668408/article/details/113671170
"""
import tkinter
import tkinter.ttk
import os
# -*- coding: utf-8 -*-

__author__ = 'CleaverCreator'


class Main:
    def __init__(self):
        self.window = tkinter.Tk()
        self.FileTree = tkinter.ttk.Treeview(self.window, columns='none')
        self.Project = str
        win_width = 1920
        win_height = 1005
        screen_width, screen_height = self.window.maxsize()
        x = int((screen_width - win_width) / 2)
        y = int((screen_height - win_height) / 2)
        self.window.title("UNDL IDE")
        self.window.geometry("%sx%s+%s+%s" % (win_width, win_height, x, y))
        self.Menu = tkinter.Menu(self.window)
        self.window.config(menu=self.Menu)

    def file_tree(self, project):
        self.Project = project
        self.FileTree.heading('#0', text='Event', anchor=tkinter.W)
        if not os.listdir(self.Project):
            return 'NOT PROJECT'
        else:
            for i in os.listdir(self.Project):
                self.Project = project
                on_fielder = ''
                path_file = os.path.join(self.Project, i)
                if os.path.isdir(path_file):
                    self.file_tree(path_file)
                    on_fielder = self.FileTree.insert('', index=tkinter.END, text=path_file, open=True)
                else:
                    self.FileTree.insert(on_fielder, tkinter.END, text=path_file)
        self.FileTree.pack()

    def main_loop(self):
        return self.window.mainloop()
