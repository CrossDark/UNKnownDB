import sys
from PyQt5.QtWidgets import *


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'UNDL IDE'
        self.left = 0
        self.top = 40
        self.width = 1900
        self.height = 1020
        self.init_ui()
        self.model = None
        self.tree = None
        self.app = None
        self.setLayout = None
        self.TableWidget = None
        self.layout = None

    def init_ui(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.model = QFileSystemModel()
        self.model.setRootPath('')
        self.tree = QTreeView()
        self.tree.setModel(self.model)
        self.tree.setAnimated(False)
        for i in [1, 2, 3]:
            self.tree.setColumnHidden(i, True)
        self.tree.setIndentation(10)
        self.tree.setSortingEnabled(True)
        self.tree.setWindowTitle("Event")
        self.tree.resize(400, 1000)
        window_layout = QVBoxLayout()
        window_layout.addWidget(self.tree)
        self.setLayout(window_layout)
        self.show()


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setCentralWidget(App())


if __name__ != '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
