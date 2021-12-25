import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap


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


class Tools(QToolBar):
    def __init__(self):
        super(Tools, self).__init__()
        action = QAction(QIcon('./Image/run.ico'), "Run", self)
        self.addAction(action)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.pressed = None
        self.setCentralWidget(App())
        self.resize(1910, 1010)
        self.status = self.statusBar()
        self.status.showMessage('Nothing')
        # 菜单栏
        menu_bar = self.menuBar()
        menu = menu_bar.addMenu("File")
        action = QAction(QIcon("./Image/run.ico"), "New Project", self)
        menu.addAction(action)
        menu2 = menu.addMenu("Add to ...")
        menu2.addAction(QAction("workspace edit...", self))
        # 工具栏
        tool = self.addToolBar("File")
        run = QAction(QIcon("/home/pi/PycharmProjects/UNKnownDB/UNKnownDB/UNDL/APP/Image/run.ico"), "run", self)
        tool.addAction(run)
        tool.actionTriggered[QAction].connect(self.tool_btn_pressed)
        self.show()

    def tool_btn_pressed(self, q_action):
        self.pressed = ("pressed too btn is", q_action.text())


if __name__ != '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(''))
    ex = MainWindow()
    sys.exit(app.exec_())
