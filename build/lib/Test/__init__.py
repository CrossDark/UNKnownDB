# import DB
from UNKnownDB import DB

with DB.LocalDB('./.Clever.unp/Guide.unp') as db:
    db
    print(db.FormApply)
