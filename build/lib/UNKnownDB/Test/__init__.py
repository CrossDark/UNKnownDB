# import DB
from UNKnownDB.UNDL import Interpreter
# from UNKnownDB import DB


with open('./.Clever.unp/Guide.undl') as code:
    lines = code.readlines()
inter = Interpreter.Interpret(lines)
inter.dictionary()
form = Interpreter.Form(inter.Form, inter.FormDict)
print(form.type())
print(form.Form)


# db = DB.LocalDB("./.Clever.unp")
# db.create()
