# tkinter：文件系统遍历
import tkinter as tk
import os
from time import sleep


class DirList(object):
    def __init__(self, init_dir=os.curdir):
        self.top = tk.Tk()
        self.top.title('查找')

        self.last = None

        self.top.geometry('400x500')  # 设置窗口大小
        self.label = tk.Label(self.top, text='文件列表', font='宋体 -16 bold')
        self.label.pack()

        # StringVar：字符串变量，特点是跟踪变量变化，及时显示在界面上
        self.cwd = tk.StringVar(self.top)
        self.cwd.set(init_dir)

        # 当前目录显示标签
        self.dir_l = tk.Label(self.top, fg='blue', font='Helvetica -14 bold')
        self.dir_l.pack()

        # 新建框体容器，存放文件列表和滚动条
        self.dir_fm = tk.Frame(self.top)
        # 滚动条
        self.dir_sb = tk.Scrollbar(self.dir_fm)
        self.dir_sb.pack(side=tk.RIGHT, fill=tk.Y)
        # 列表框
        self.dirs = tk.Listbox(self.dir_fm, height=23, width=60,
                               font='Helvetica -14',
                               yscrollcommand=self.dir_sb.set)
        # 绑定setDirAndGo函数
        self.dirs.bind('<Double-1>', self.setDirAndGo)
        # 滑动框与列表关联
        self.dir_sb.config(command=self.dirs.yview)
        self.dirs.pack(side=tk.LEFT, fill=tk.X)
        self.dir_fm.pack(fill=tk.BOTH)

        # 输入框
        self.dirn = tk.Entry(self.top, width=60, font='Helvetica -14',
                             textvariable=self.cwd)
        # 监听回车事件，绑定doLS函数，函数必须要有event参数
        self.dirn.bind('<Return>', self.doLS)
        self.dirn.pack(fill=tk.BOTH)

        # 功能按钮框架包括三个按钮：清除、查询和退出。
        self.bfm = tk.Frame(self.top)
        self.clr = tk.Button(self.bfm, text='清除', width=6, command=self.clrDir,
                             activeforeground='white', activebackground='blue')
        self.ls = tk.Button(self.bfm, text='查询', width=6, command=self.doLS,
                            activeforeground='white', activebackground='green')
        self.quit = tk.Button(self.bfm, text='退出', width=6, command=self.top.quit,
                              activeforeground='white', activebackground='red')
        self.clr.pack(side=tk.LEFT, fill=tk.BOTH)
        self.ls.pack(side=tk.LEFT, fill=tk.BOTH)
        self.quit.pack(side=tk.LEFT, fill=tk.BOTH)
        self.bfm.pack()

    def clrDir(self, ev=None):
        """清空文件路径输入框"""
        self.cwd.set('')

    def setDirAndGo(self, ev=None):
        """设置文件路径并查询"""
        self.last = self.cwd.get()
        # 选中项背景默认为红色，后续修改为蓝色
        self.dirs.config(selectbackground='red')
        # 获取文件列表中选择项，没有选则输入框设置为当前目录路径
        try:
            # 获取目录列表中选中的文件名
            check = self.dirs.get(self.dirs.curselection())
        except FileNotFoundError:
            return "没有文件或文件错误!"

        if not check:
            check = os.curdir
        self.cwd.set(check)
        self.doLS()

    def doLS(self, event=''):
        """
        查询文件路径
        :param event:输入框回车事件触发参数
        :return:无
        """
        error = ''
        tdir = self.cwd.get()
        if not tdir:
            tdir = os.curdir

        # 判断输入框中文件是否存在
        if not os.path.exists(tdir):
            error = tdir + ': no such file!'
        # 若文件存在，再判断是否是目录
        elif not os.path.isdir(tdir):
            error = tdir + ' is not directory!'

        if error:
            '''出现错误则提示在输入框内，2秒后还原'''
            self.dirn.config(fg='red')  # 输入框提示文字变为红色
            self.cwd.set(error)
            self.top.update()
            sleep(2)
            if not (hasattr(self, 'last') and self.last):
                '''使用hasattr函数判断对象是否含有last属性或方法'''
                self.last = os.curdir
            self.cwd.set(self.last)
            self.dirs.config(selectbackground='LightSkyBlue')
            self.dirn.config(fg='black')  # 输入框文字颜色还原
            self.top.update()
            return

        self.cwd.set('FETCHING DIRECTORY CONTENTS...')
        self.top.update()

        '''目录列表框操作'''
        self.dirs.delete(0, tk.END)  # 清空目录列表
        # self.dirs.insert(tk.END, os.cur-dir) # 添加当前目录"."
        self.dirs.insert(tk.END, os.pardir)  # 添加上级目录".."

        '''获取指定目录下的文件，在列表控件展示'''
        dirlist = os.listdir(tdir)
        dirlist.sort()
        os.chdir(tdir)  # 改变目录到指定路径
        for eachFile in dirlist:
            self.dirs.insert(tk.END, eachFile)
        self.cwd.set(os.getcwd())  # 在输入框中显示当前绝对路径
        self.dir_l.config(text=os.getcwd())  # 上方标签显示当前路径
        self.dirs.config(selectbackground='LightSkyBlue')  # 选中时背景色为蓝色
        self.last = self.cwd.get()  # 记录最后一次路径


def main():
    DirList('D:\\')
    tk.mainloop()


if __name__ == '__main__':
    main()
