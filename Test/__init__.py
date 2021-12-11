# import DB
import UNDL.Interpreter
undl = UNDL.Interpreter.Form('./.Clever.unp/Guide.unp')
guide = UNDL.Interpreter.Guide('./.Clever.unp/Guide.unp')
print(undl.Code)
print(guide.port())
print(undl.form())
print(undl.create_form())
