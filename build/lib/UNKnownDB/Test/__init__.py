# import DB
from UNKnownDB import DB

DB.LocalDB('.Clever.unp').create()
with DB.LocalDB('./.Clever.unp/Guide.unp') as db:
    db
    print(db.FormApply)
