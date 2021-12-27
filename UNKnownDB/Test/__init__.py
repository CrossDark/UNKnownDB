# import DB
from UNKnownDB.UNDL import Interpreter, APP
# from UNKnownDB import DB


with open('./.Clever.unp/Guide.undl') as code:
    lines = code.readlines()
inter = Interpreter.Interpret(lines)
inter.dictionary()
form = Interpreter.Form(inter.Form, inter.FormDict)
inter.dictionary()
app = APP.Tree()
app.init_ui()
# db = DB.LocalDB("./.Clever.unp")
# db.create()
