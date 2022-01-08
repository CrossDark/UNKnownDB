# import DB
# from UNKnownDB.UNDL import Interpreter, APP
from UNKnownDB.DB import LightDB

with LightDB.Data('./light') as db:
    db + 'ed:de'
    db - 'ed:de'
    db['fe'] = 'ef0'
    for print_ in db.find():
        print(print_)

with open('./light.unl') as light:
    print(light.read())
# db = DB.LocalDB("./.Clever.unp")
# db.create()
