# import DB
from UNKnownDB.UNDL import Interpreter, APP
# from UNKnownDB import DB


with open('./.Clever.unp/Guide.undl') as code:
    lines = code.readlines()
inter = Interpreter.Interpret(lines)
inter.dictionary()
form = Interpreter.Form(inter.Form, inter.FormDict)
app = APP.Main()
app.file_tree('./.Clever.unp')
app.main_loop()


# db = DB.LocalDB("./.Clever.unp")
# db.create()
