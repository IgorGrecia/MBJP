import os

filename = "fixcobpl.py"
with open(filename, "rb") as source_file:
    code = compile(source_file.read(), filename, "exec")
exec(code)

filename = "fixcam.py"
with open(filename, "rb") as source_file:
    code = compile(source_file.read(), filename, "exec")
exec(code)

filename = "fixmat.py"
with open(filename, "rb") as source_file:
    code = compile(source_file.read(), filename, "exec")
exec(code)

filename = "fixbook.py"
with open(filename, "rb") as source_file:
    code = compile(source_file.read(), filename, "exec")
exec(code)

filename = "fixhr.py"
with open(filename, "rb") as source_file:
    code = compile(source_file.read(), filename, "exec")
exec(code)