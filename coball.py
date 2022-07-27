import os
from playsound import playsound

filename = "fixcobpl.py"
with open(filename, "rb") as source_file:
    code = compile(source_file.read(), filename, "exec")
exec(code)

print("Parcela + Lanches")
playsound('dog.mp3')
test = input("Run = 0\nSkip = 1\n")

if test == "0":
    filename = "cobpl.py"
    with open(filename, "rb") as source_file:
        code = compile(source_file.read(), filename, "exec")
    exec(code)

filename = "fixhr.py"
with open(filename, "rb") as source_file:
    code = compile(source_file.read(), filename, "exec")
exec(code)

print("Home Reading")
playsound('dog.mp3')
test = input("Run = 0\nSkip = 1\n")

if test == "0":
    filename = "cobhr.py"
    with open(filename, "rb") as source_file:
        code = compile(source_file.read(), filename, "exec")
    exec(code)

filename = "fixcam.py"
with open(filename, "rb") as source_file:
    code = compile(source_file.read(), filename, "exec")
exec(code)

print("Camisetas")
playsound('dog.mp3')
test = input("Run = 0\nSkip = 1\n")

if test == "0":
    filename = "cobcam.py"
    with open(filename, "rb") as source_file:
        code = compile(source_file.read(), filename, "exec")
    exec(code)

filename = "fixmat.py"
with open(filename, "rb") as source_file:
    code = compile(source_file.read(), filename, "exec")
exec(code)

print("Matific App")
playsound('dog.mp3')
test = input("Run = 0\nSkip = 1\n")

if test == "0":
    filename = "cobmat.py"
    with open(filename, "rb") as source_file:
        code = compile(source_file.read(), filename, "exec")
    exec(code)

filename = "fixbook.py"
with open(filename, "rb") as source_file:
    code = compile(source_file.read(), filename, "exec")
exec(code)

print("Perda Livros")
playsound('dog.mp3')
test = input("Run = 0\nSkip = 1\n")

if test == "0":
    filename = "cobbook.py"
    with open(filename, "rb") as source_file:
        code = compile(source_file.read(), filename, "exec")
    exec(code)