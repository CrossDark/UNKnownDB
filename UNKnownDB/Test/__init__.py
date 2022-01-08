# import DB
# from UNKnownDB.UNDL import Interpreter, APP
from UNKnownDB.DB import LightDB

with LightDB.Data('light') as db:
    db + 'ed:de'
    db - 'ed:de'
    db['fge'] = 'ef0'
    db.find()
    print(db.path)

with open('./light.unl') as light:
    print(light.read())
    pass
# db = DB.LocalDB("./.Clever.unp")
# db.create()
