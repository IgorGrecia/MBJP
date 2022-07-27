import sys
import os

if os.path.isfile("Text\\FixingLembretes.txt"):
    os.remove("Text\\FixingLembretes.txt")
ffix = open("Text\\FixingLembretes.txt", "w",encoding='utf8')
fnames = open("Text\\Names.txt", "r",encoding='utf8')
names = fnames.read()

pathinf = 'Infantil'
pathfund1 = 'Fundamental\\1'
pathfund2 = 'Fundamental\\2'
pathfund3 = 'Fundamental\\3'

finf = os.listdir(pathinf)
ffund1 = os.listdir(pathfund1)
ffund2 = os.listdir(pathfund2)
ffund3 = os.listdir(pathfund3)

ffix.write("Inf")
ffix.write("\n")
for line in names.splitlines():
    if any(line in s for s in finf):
        ffix.write(line)
        ffix.write("\n")

ffix.write("Fund1")
ffix.write("\n")
for line in names.splitlines():
    if any(line in s for s in ffund1):
        ffix.write(line)
        ffix.write("\n")

ffix.write("Fund2")
ffix.write("\n")
for line in names.splitlines():
    if any(line in s for s in ffund2):
        ffix.write(line)
        ffix.write("\n")

ffix.write("Fund3")
ffix.write("\n")
for line in names.splitlines():
    if any(line in s for s in ffund3):
        ffix.write(line)
        ffix.write("\n")

fnames.close()
ffix.close()