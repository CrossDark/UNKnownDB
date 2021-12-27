# -*- coding: utf-8 -*-
from PyQt5.Qt import *
import sys


# *************占位提示文本***************开始
app = QApplication(sys.argv)

window = QWidget()
window.resize(500, 500)
window.setWindowTitle('QTextEditer学习')

text = QTextEdit(window)
text.setPlaceholderText('xxx')  # 设置提示文本
print(text.placeholderText())  # 获取提示文本
text.resize(100, 50)
text.move(200, 200)
window.show()

sys.exit(app.exec_())
# *************占位提示文本***************结束



# *************内容设置***************开始
app = QApplication(sys.argv)
#
window = QWidget()
window.resize(500, 500)
window.setWindowTitle('QTextEditer学习')

text = QTextEdit(window)
# 设置普通文本
text.setPlainText('123')  # 设置普通文本
print(text.toPlainText())  # 获取文本框内容
text.resize(100, 50)
text.move(200, 200)
#
# # 设置富文本
text.setHtml('<h1>ooo<h1>')  # 设置富文本
print(text.toHtml())  #获取富文本
text.resize(100, 50)
text.move(200, 200)
#
def cao():
    # text.insertPlainText('789')  #插入文本
    text.insertHtml('<h1>235<h1>')  #插入文本
    text.clear()  # 清除文本内容
    btn = QPushButton(window)
    btn.setText('按钮')
    btn.resize(50, 50)
    btn.clicked.connect(cao)
#
def cao1():
    text.append('<h1>369<h1>')  # 富文本无法使用
#
    btn1 = QPushButton(window)
    btn1.setText('按钮')
    btn1.resize(50, 50)
    btn1.move(0,100)
    btn1.clicked.connect(cao1)
#
    window.show()
#
    sys.exit(app.exec_())
# *************内容设置***************结束

# *************自动化格式***************开始
app = QApplication(sys.argv)
#
window = QWidget()
window.resize(500, 500)
window.setWindowTitle('QTextEditer学习')
#
text = QTextEdit(window)
text.setPlaceholderText('xxx')  # 设置提示文本
print(text.placeholderText())  # 获取提示文本
text.resize(100, 50)
text.move(200, 200)
text.setAutoFormatting(QTextEdit.AutoBulletList)  # 自动创建项目符号列表
text.setAutoFormatting(QTextEdit.AutoAll) # 所有自动测试
window.show()
#
sys.exit(app.exec_())
# *************自动化格式***************结束

# ***************软换行模式*************开始
app = QApplication(sys.argv)
#
window = QWidget()
window.resize(500, 500)
window.setWindowTitle('QTextEditer学习')
#
text = QTextEdit(window)
text.setPlaceholderText('xxx')  # 设置提示文本
print(text.placeholderText())  # 获取提示文本
text.resize(100, 50)
text.move(200, 200)
text.setLineWrapMode(QTextEdit.NoWrap)  # 设置换行
print(text.lineWrapMode())  # 获取软换行
text.setWordWrapMode(QTextOption.WordWrap)  # 设置单词换行模式
print(text.wordWrapMode())
#
window.show()
#
sys.exit(app.exec_())
# *************软换行模式***************结束



# *************覆盖模式设置***************开始
覆盖模式即键盘的insert功能
app = QApplication(sys.argv)

window = QWidget()
window.resize(500, 500)
window.setWindowTitle('QTextEditer学习')

text = QTextEdit(window)
text.setPlaceholderText('xxx')  # 设置提示文本
print(text.placeholderText())  # 获取提示文本
text.setOverwriteMode(True)
text.resize(100, 50)
text.move(200, 200)
#
window.show()
#
sys.exit(app.exec_())
# *************覆盖模式设置***************结束

# *************字体格式***************开始
app = QApplication(sys.argv)
#
window = QWidget()
window.resize(500, 500)
window.setWindowTitle('QTextEditer学习')
#
text = QTextEdit(window)
text.setPlaceholderText('xxx')  # 设置提示文本
print(text.placeholderText())  # 获取提示文本
text.resize(100, 50)
text.move(200, 200)
text.setFontFamily('幼圆')  # 设置字体
text.setFontWeight(QFont.Black)  #设置字体粗细
text.setFontItalic(True)  # 设置斜体
text.setFontPointSize(15)  # 设置字体大小
text.setFontUnderline(True)  # 设置下划线
#
QFontDialog.getFont()  #查可用字体
#
window.show()
#
sys.exit(app.exec_())
# *************字体格式***************结束



# *************颜色设置***************开始
# app = QApplication(sys.argv)
#
# window = QWidget()
# window.resize(500, 500)
# window.setWindowTitle('QTextEditer学习')
#
# text = QTextEdit(window)
# text.setPlaceholderText('xxx')  # 设置提示文本
# print(text.placeholderText())  # 获取提示文本
# text.resize(100, 50)
# text.move(200, 200)
# text.setTextBackgroundColor(QColor(200, 10, 10))  #设置文本背景颜色
# text.setTextColor(QColor(10, 200, 10))  # 设置字体颜色
#
# window.show()
#
# sys.exit(app.exec_())
# *************颜色设置***************结束

# *************对齐方式***************开始
# app = QApplication(sys.argv)
#
# window = QWidget()
# window.resize(500, 500)
# window.setWindowTitle('QTextEditer学习')
#
# text = QTextEdit(window)
# text.setPlaceholderText('xxx')  # 设置提示文本
# print(text.placeholderText())  # 获取提示文本
# text.resize(100, 50)
# text.move(200, 200)
# text.setAlignment(Qt.AlignCenter)  # 设置文本对齐方式
#
# window.show()
#
# sys.exit(app.exec_())
# *************对齐方式***************结束

# *************光标设置***************开始
# app = QApplication(sys.argv)
#
# window = QWidget()
# window.resize(500, 500)
# window.setWindowTitle('QTextEditer学习')
#
# text = QTextEdit(window)
# text.setPlaceholderText('xxx')  # 设置提示文本
# print(text.placeholderText())  # 获取提示文本
# text.resize(100, 50)
# text.move(200, 200)
# text.setCursorWidth(10)
#
# window.show()
#
# sys.exit(app.exec_())
# *************光标设置***************结束



# *************只读设置***************开始
# app = QApplication(sys.argv)
#
# window = QWidget()
# window.resize(500, 500)
# window.setWindowTitle('QTextEditer学习')
#
# text = QTextEdit(window)
# text.setPlaceholderText('xxx')  # 设置提示文本
# print(text.placeholderText())  # 获取提示文本
# text.resize(100, 50)
# text.move(200, 200)
# text.setReadOnly(True)  # 设置只读
#
# window.show()
#
# sys.exit(app.exec_())
# *************只读设置***************结束