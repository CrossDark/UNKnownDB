# -*- coding: utf-8 -*-
import markdown2 as markdown2
from PyQt5.Qt import *


class Dialog_main(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):

        super(Dialog_main, self).__init__(parent)
        self.setupUi(self)
    def md2html(self, mdstr):
        extras = ['code-friendly', 'fenced-code-blocks', 'footnotes','tables','code-color','pyshell','nofollow','cuddled-lists','header ids','nofollow']

        html = """
        <html>
        <head>
        <meta content="text/html; charset=utf-8" http-equiv="content-type" />
        <style>
            .hll { background-color: #ffffcc }
            .c { color: #0099FF; font-style: italic } /* Comment */
            .err { color: #AA0000; background-color: #FFAAAA } /* Error */
            .k { color: #006699; font-weight: bold } /* Keyword */
            .o { color: #555555 } /* Operator */
            .ch { color: #0099FF; font-style: italic } /* Comment.Hashbang */
            <!--省略一大堆的CSS样式-->
        </style>
        </head>
        <body>
            %s
        </body>
        </html>
        """

        ret = markdown2.markdown(mdstr, extras=extras)
        return html % ret

    @pyqtSlot()
    def on_plainTextEdit_textChanged(self):
        md = self.plainTextEdit.toPlainText()
        newhtml = self.md2html(md)
        self.textEdit.setHtml(newhtml)