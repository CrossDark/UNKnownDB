import sys

from PyQt5.Qt import *


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


class File(QWidget):
    def __init__(self):
        super(File, self).__init__()
        self.textEdit = None

    def text(self):
        self.textEdit = QTextEdit()
        self.textEdit.setGeometry(100, 100, 100, 30)

        # 创建一个布局管理器
        self.setWindowTitle('File Edit')
        window_layout = QVBoxLayout()
        window_layout.addWidget(self.textEdit)
        self.setLayout(window_layout)
        self.show()


class SPL(QSplitter):
    def __init__(self):
        super(SPL, self).__init__()
        self.addWidget(App())
        file = File()
        file.text()
        self.addWidget(file)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.pressed = None
        self.setCentralWidget(SPL())
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
        #
        self.status = QStatusBar()
        self.setStatusBar(self.status)
        #
        self.setWindowState(Qt.WindowMaximized)
        self.show()

    def tool_btn_pressed(self, q_action):
        self.pressed = str("pressed too btn is " + q_action.text())
        if q_action == 'run':
            pass
        self.status.showMessage(self.pressed)


if __name__ != '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(''))
    ex = MainWindow()
    sys.exit(app.exec_())
