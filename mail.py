import os

filename = "fixmail.py"
with open(filename, "rb") as source_file:
    code = compile(source_file.read(), filename, "exec")
exec(code)
filename = "checkmail.py"
with open(filename, "rb") as source_file:
    code = compile(source_file.read(), filename, "exec")
exec(code)
filename = "checkmailhr.py"
with open(filename, "rb") as source_file:
    code = compile(source_file.read(), filename, "exec")
exec(code)
filename = "checkmailcam.py"
with open(filename, "rb") as source_file:
    code = compile(source_file.read(), filename, "exec")
exec(code)
filename = "checkmailmat.py"
with open(filename, "rb") as source_file:
    code = compile(source_file.read(), filename, "exec")
exec(code)
filename = "checkmailbook.py"
with open(filename, "rb") as source_file:
    code = compile(source_file.read(), filename, "exec")
exec(code)