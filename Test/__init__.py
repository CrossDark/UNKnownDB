# import DB
import DB


with DB.LocalDB('./.Clever.unp/Guide.unp') as db:
    db.form()
    db.create_form()
    print(db.FormApply)
