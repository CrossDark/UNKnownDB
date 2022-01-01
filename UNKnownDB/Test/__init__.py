# import DB
# from UNKnownDB.UNDL import Interpreter, APP
from UNKnownDB.DB import LightDB


with LightDB.File('./light') as db:
    db += ''
with open('./light') as light:
    print(light.read())
# db = DB.LocalDB("./.Clever.unp")
# db.create()
