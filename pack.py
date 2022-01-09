import os
import time
import re
from UNKnownDB.DB import LocalDB

with open('./setup.py', 'r+') as setup:
    setup.seek(0, 0)
    find = re.findall('version=(.+?),', setup.read())
    setup.write(setup.read().replace(str(float(find[0] + 0.01)), 'utf-8'))
os.system('python3 setup.py sdist bdist_wheel')
time.sleep(5)
os.system('twine upload dist/* --u CleverCreator --p Bitjop-byfbeg-3sazry')
time.sleep(5)
db = LocalDB('')
db.delete_all('./dist')
