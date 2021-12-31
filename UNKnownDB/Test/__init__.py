# import DB
# from UNKnownDB.UNDL import Interpreter, APP
from UNKnownDB.DB import LightDB


with LightDB.File('./light') as db:
    db += 'l'
    print(db.DB)
# db = DB.LocalDB("./.Clever.unp")
# db.create()
