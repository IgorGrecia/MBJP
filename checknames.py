import sys
import os

if os.path.isfile("Text\\Fixing.txt"):
    os.remove("Text\\Fixing.txt")
ffix = open("Text\\Fixing.txt", "w",encoding='utf8')
fnames = open("Text\\Names.txt", "r",encoding='utf8')
names = fnames.read()
fmbat = open("Text\\MB At.txt", "r",encoding='utf8')
mbat = fmbat.read()
fmbinat = open("Text\\MB Inat.txt", "r",encoding='utf8')
mbinat = fmbinat.read()
fmbfat = open("Text\\MBF At.txt", "r",encoding='utf8')
mbfat = fmbfat.read()
fmbfinat = open("Text\\MBF Inat.txt", "r",encoding='utf8')
mbfinat = fmbfinat.read()
fmbhr = open("Text\\HR MB.txt", "r",encoding='utf8')
mbhr = fmbhr.read()
fmbfhr = open("Text\\HR MBF.txt", "r",encoding='utf8')
mbfhr = fmbfhr.read()
fmbcam = open("Text\\Cam MB.txt", "r",encoding='utf8')
mbcam = fmbcam.read()
fmbfcam = open("Text\\Cam MBF.txt", "r",encoding='utf8')
mbfcam = fmbfcam.read()
fmbmat = open("Text\\Mat MB.txt", "r",encoding='utf8')
mbmat = fmbmat.read()
fmbfmat = open("Text\\Mat MBF.txt", "r",encoding='utf8')
mbfmat = fmbfmat.read()
fmbbook = open("Text\\Book MB.txt", "r",encoding='utf8')
mbbook = fmbbook.read()
fmbfbook = open("Text\\Book MBF.txt", "r",encoding='utf8')
mbfbook = fmbfbook.read()

ffix.write("MB At")
ffix.write("\n")
for line in names.splitlines():
    if mbat.find(line)!=-1:
        ffix.write(line)
        ffix.write("\n")

ffix.write("MB Inat")
ffix.write("\n")
for line in names.splitlines():
    if mbinat.find(line)!=-1:
        ffix.write(line)
        ffix.write("\n")

ffix.write("MBF At")
ffix.write("\n")
for line in names.splitlines():
    if mbfat.find(line)!=-1:
        ffix.write(line)
        ffix.write("\n")

ffix.write("MBF Inat")
ffix.write("\n")
for line in names.splitlines():
    if mbfinat.find(line)!=-1:
        ffix.write(line)
        ffix.write("\n")

ffix.write("MB HR")
ffix.write("\n")
for line in names.splitlines():
    if mbhr.find(line)!=-1:
        ffix.write(line)
        ffix.write("\n")

ffix.write("MBF HR")
ffix.write("\n")
for line in names.splitlines():
    if mbfhr.find(line)!=-1:
        ffix.write(line)
        ffix.write("\n")

ffix.write("MB Cam")
ffix.write("\n")
for line in names.splitlines():
    if mbcam.find(line)!=-1:
        ffix.write(line)
        ffix.write("\n")

ffix.write("MBF Cam")
ffix.write("\n")
for line in names.splitlines():
    if mbfcam.find(line)!=-1:
        ffix.write(line)
        ffix.write("\n")

ffix.write("MB Mat")
ffix.write("\n")
for line in names.splitlines():
    if mbmat.find(line)!=-1:
        ffix.write(line)
        ffix.write("\n")

ffix.write("MBF Mat")
ffix.write("\n")
for line in names.splitlines():
    if mbfmat.find(line)!=-1:
        ffix.write(line)
        ffix.write("\n")

ffix.write("MB Book")
ffix.write("\n")
for line in names.splitlines():
    if mbbook.find(line)!=-1:
        ffix.write(line)
        ffix.write("\n")

ffix.write("MBF Book")
ffix.write("\n")
for line in names.splitlines():
    if mbfbook.find(line)!=-1:
        ffix.write(line)
        ffix.write("\n")

ffix.close()
fnames.close()
fmbat.close()
fmbinat.close()
fmbfat.close()
fmbfinat.close()
fmbhr.close()
fmbfhr.close()
fmbcam.close()
fmbfcam.close()
fmbmat.close()
fmbfmat.close()
fmbbook.close()
fmbfbook.close()