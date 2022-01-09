# import DB
# from UNKnownDB.UNDL import Interpreter, APP
from UNKnownDB.DB import LightDB
from UNKnownDB.DSL import Main


with LightDB.Data('light') as db:
    for x in db:
        print(x)

with open('./light.unl') as light:
    print(light.read())

main = Main(
    'd:ww\ndw:p'
            )
# db = DB.LocalDB("./.Clever.unp")
# db.create()
