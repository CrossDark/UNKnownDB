# import DB
from UNKnownDB.UNDL import Interpreter, APP
# from UNKnownDB import DB


with open('./.Clever.unp/Guide.undl') as code:
    lines = code.readlines()
inter = Interpreter.Interpret(lines)
inter.dictionary()
form = Interpreter.Form(inter.Form, inter.FormDict)
inter.dictionary()
app = APP.App()
app.init_ui()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
# db = DB.LocalDB("./.Clever.unp")
# db.create()
