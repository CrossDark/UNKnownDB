# import DB
# from UNKnownDB.UNDL import Interpreter, APP
from UNKnownDB.DB import LightDB

with LightDB.Data('light') as db:
    del db['try']
    print(db)

with open('./light.unl') as light:
    print(light.read())
# db = DB.LocalDB("./.Clever.unp")
# db.create()
