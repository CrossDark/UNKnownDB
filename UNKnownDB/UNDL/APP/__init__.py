import sys
from PyQt5.QtWidgets import QApplication, QFileSystemModel, QTreeView, QWidget, QVBoxLayout, QTableWidget


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'UNDL IDE'
        self.left = 0
        self.top = 40
        self.width = 1920
        self.height = 1040
        self.init_ui()
        self.model = None
        self.tree = None
        self.app = None

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


class TextEdit(QWidget):
    def __init__(self):
        super(TextEdit, self).__init__()


if __name__ != '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
