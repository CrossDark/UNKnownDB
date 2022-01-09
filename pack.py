import os
import time
import re
from UNKnownDB.DB import LocalDB

with open('./setup.py', 'r+') as setup:
    setup.seek(0, 0)
    read = setup.read()
    find = re.findall('version=(.+?),', read)
    v_id = float(eval(find[0].replace('.', '')))
    setup.seek(0, 0)
    writing = read.replace(find[0], "'" + str(v_id + 1) + "'")
    setup.write(writing[:-1])
# os.system('python3 setup.py sdist bdist_wheel')
time.sleep(5)
# os.system('twine upload dist/* --u CleverCreator --p Bitjop-byfbeg-3sazry')
time.sleep(5)
db = LocalDB('')
db.delete_all('./dist')
