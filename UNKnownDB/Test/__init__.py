# import DB
from UNKnownDB.UNDL import Interpreter
from UNKnownDB import DB


db = Interpreter.Form("./.Clever.unp/Guide.undl")
guide = Interpreter.Guide("./.Clever.unp/Guide.undl")
print(guide.name())
db.base()
print(db.create())
print(db.index())
