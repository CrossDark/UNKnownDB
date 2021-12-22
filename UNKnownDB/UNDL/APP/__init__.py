"""
thanks:https://blog.csdn.net/weixin_39668408/article/details/113671170
theme_color = {
    'Default': '#000000.#FFFFFF',
    'Grey model': '#83406A.#D1D4D1',
    'Aquamarine': '#5B8340.#D1E7E0',
    'Bold Beige': '#4B4620.#FFF0E1',
    'Cobalt Blue': '#ffffBB.#3333aa',
    'Olive Green': '#D1E7E0.#5B8340',
    'Night Mode': '#FFFFFF.#000000',
}


class EditorPlus(Tk):
    def __init__(self):
        super().__init__()
        self._set_window_()
        self._create_menu_bar_()
        self._create_shortcut_bar_()
        self._create_body_()

    # 设置初始窗口的属性
    def _set_window_(self):
        self.title("EditorPlus")
        self.geometry('650x450')

    # 创建整个菜单栏
    def _create_menu_bar_(self):
        menu_bar = Menu(self)
        # 创建文件的联级菜单
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label='新建', accelerator='Ctrl+N')
        file_menu.add_command(label='打开', accelerator='Ctrl+O')
        file_menu.add_command(label='保存', accelerator='Ctrl+S')
        file_menu.add_command(label='另存为', accelerator='Shift+Ctrl+S')
        file_menu.add_separator()
        file_menu.add_command(label='退出', accelerator='Alt+F4')

        # 在菜单栏上添加菜单标签，并将该标签与相应的联级菜单关联起来
        menu_bar.add_cascade(label='文件', menu=file_menu)

        # 创建编辑的联级菜单
        edit_menu = Menu(menu_bar, tearoff=0)
        edit_menu.add_command(label='撤销', accelerator='Ctrl+Z')
        edit_menu.add_command(label='恢复', accelerator='Ctrl+Y')
        edit_menu.add_separator()
        edit_menu.add_command(label='剪切', accelerator='Ctrl+X')
        edit_menu.add_command(label='复制', accelerator='Ctrl+C')
        edit_menu.add_command(label='粘贴', accelerator='Ctrl+V')
        edit_menu.add_separator()
        edit_menu.add_command(label='查找', accelerator='Ctrl+F')
        edit_menu.add_separator()
        edit_menu.add_command(label='全选', accelerator='Ctrl+A')
        menu_bar.add_cascade(label='编辑', menu=edit_menu)

        # 视图菜单
        view_menu = Menu(menu_bar, tearoff=0)
        show_line_number = IntVar()
        show_line_number.set(1)
        view_menu.add_checkbutton(label='显示行号', variable=show_line_number)

        highlight_line = IntVar()
        view_menu.add_checkbutton(label='高亮当前行', onvalue=1, offvalue=0, variable=highlight_line)

        # 在主题菜单中再添加一个子菜单列表
        themes_menu = Menu(menu_bar, tearoff=0)
        view_menu.add_cascade(label='主题', menu=themes_menu)

        theme_choice = StringVar()
        theme_choice.set('Default')
        for k in sorted(theme_color):
            themes_menu.add_radiobutton(label=k, variable=theme_choice)

        menu_bar.add_cascade(label='视图', menu=view_menu)

        about_menu = Menu(menu_bar, tearoff=0)
        about_menu.add_command(label='关于')
        about_menu.add_command(label='帮助')
        menu_bar.add_cascade(label='关于', menu=about_menu)
        self["menu"] = menu_bar

    # 创建快捷菜单栏
    def _create_shortcut_bar_(self):
        shortcut_bar = Frame(self, height=25, background='#20b2aa')
        shortcut_bar.pack(fill='x')

    # 创建程序主体
    def _create_body_(self):
        # 创建行号栏 （take focus=0 屏蔽焦点）
        line_number_bar = Text(self, width=4, padx=3, takefocus=0, border=0,
                               background='#F0E68C', state='disabled')
        line_number_bar.pack(side='left', fill='y')

        # 创建文本输入框
        content_text = Text(self, wrap='word')
        content_text.pack(expand=True, fill='both')

        # 创建滚动条
        scroll_bar = Scrollbar(content_text)
        scroll_bar["command"] = content_text.yview
        content_text["yscrollcommand"] = scroll_bar.set
        scroll_bar.pack(side='right', fill='y')


if "__main__" == __name__:
    app = EditorPlus()
    app.mainloop()
"""


import tkinter
import tkinter.ttk
import os
# -*- coding: utf-8 -*-

__author__ = 'CleaverCreator'


class Main:
    def __init__(self):
        self.window = tkinter.Tk()
        self.FileTreeBox = tkinter.Frame(width=200, height=720, relief='groove', borderwidth=5)
        self.FileTree = tkinter.ttk.Treeview(self.FileTreeBox, columns='none')
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
        self.FileTree.heading('#0', text='文件', anchor=tkinter.W)
        if not os.listdir(self.Project):
            return 'NOT PROJECT'
        else:
            on_fielder = self.FileTree.insert('', index=tkinter.END, text=project, open=True)
            for i in os.listdir(self.Project):
                self.Project = project
                path_file = os.path.join(self.Project, i)
                if os.path.isfile(path_file):
                    self.FileTree.insert(on_fielder, tkinter.END, text=i)
                else:
                    self.file_tree(path_file)
                    on_fielder = self.FileTree.insert('', index=tkinter.END, text=i, open=True)
        self.FileTree.pack()
        self.FileTreeBox.pack()

    def main_loop(self):
        return self.window.mainloop()
