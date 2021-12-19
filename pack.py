import os
import time
from UNKnownDB.DB import LocalDB


os.system('python3 setup.py sdist bdist_wheel')
time.sleep(10)
os.system('twine upload dist/* --u CleverCreator --p Bitjop-byfbeg-3sazry')
time.sleep(10)
db = LocalDB('')
db.delete_all('./dist')
