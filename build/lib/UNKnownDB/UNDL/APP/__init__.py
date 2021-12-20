"""
UNDB
"""
import tkinter
import tkinter.ttk


root = tkinter.Tk()
root.title('small button')
style = tkinter.ttk.Style()
style.configure('button', font=14, relief='flat', background='#000000')
root.mainloop()
