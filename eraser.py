import os

test = input("Erase Mail = 0\nKeep Mail = 1\n")

f = open('Text\\HR MB.txt', 'r+')
f.truncate(0)
f = open('Text\\HR MBF.txt', 'r+')
f.truncate(0)
f = open('Text\\Book MB.txt', 'r+')
f.truncate(0)
f = open('Text\\Book MBF.txt', 'r+')
f.truncate(0)
f = open('Text\\Cam MB.txt', 'r+')
f.truncate(0)
f = open('Text\\Cam MBF.txt', 'r+')
f.truncate(0)
f = open('Text\\Mat MB.txt', 'r+')
f.truncate(0)
f = open('Text\\Mat MBF.txt', 'r+')
f.truncate(0)
f = open('Text\\MB At.txt', 'r+')
f.truncate(0)
f = open('Text\\MB Inat.txt', 'r+')
f.truncate(0)
f = open('Text\\MBF At.txt', 'r+')
f.truncate(0)
f = open('Text\\MBF Inat.txt', 'r+')
f.truncate(0)
if os.path.isfile("Text\\new.txt"):
    os.remove("Text\\new.txt")
if os.path.isfile("Text\\Fixing.txt"):
    os.remove("Text\\Fixing.txt")
if os.path.isfile("Text\\FixingLembretes.txt"):
    os.remove("Text\\FixingLembretes.txt")
if os.path.isfile("Text\\MBF At Rem HR.txt"):
    os.remove("Text\\MBF At Rem HR.txt")
if os.path.isfile("Text\\MB At Rem HR.txt"):
    os.remove("Text\\MB At Rem HR.txt")
if os.path.isfile("Text\\HR MBF Fixed.txt"):
    os.remove("Text\\HR MBF Fixed.txt")
if os.path.isfile("Text\\HR MB Fixed.txt"):
    os.remove("Text\\HR MB Fixed.txt")
if os.path.isfile("Text\\MBF At Rem MatArras.txt"):
    os.remove("Text\\MBF At Rem MatArras.txt")
if os.path.isfile("Text\\MB At Rem MatArras.txt"):
    os.remove("Text\\MB At Rem MatArras.txt")
if os.path.isfile("Text\\MBF Cam Fixed.txt"):
    os.remove("Text\\MBF Cam Fixed.txt")
if os.path.isfile("Text\\Book MB Fixed.txt"):
    os.remove("Text\\Book MB Fixed.txt")
if os.path.isfile("Text\\Book MBF Fixed.txt"):
    os.remove("Text\\Book MBF Fixed.txt")
if os.path.isfile("Text\\Cam MB Fixed.txt"):
    os.remove("Text\\Cam MB Fixed.txt")
if os.path.isfile("Text\\Cam MBF Fixed.txt"):
    os.remove("Text\\Cam MBF Fixed.txt")
if os.path.isfile("Text\\Mat MB Fixed.txt"):
    os.remove("Text\\Mat MB Fixed.txt")
if os.path.isfile("Text\\Mat MBF Fixed.txt"):
    os.remove("Text\\Mat MBF Fixed.txt")
if os.path.isfile("Text\\MB Inat Rem HR.txt"):
    os.remove("Text\\MB Inat Rem HR.txt")
if os.path.isfile("Text\\MB Inat Rem MatArras.txt"):
    os.remove("Text\\MB Inat Rem MatArras.txt")
if os.path.isfile("Text\\MBF Cam Fixed Old.txt"):
    os.remove("Text\\MBF Cam Fixed Old.txt")
if os.path.isfile("Text\\MBF Cam.txt"):
    os.remove("Text\\MBF Cam.txt")
if os.path.isfile("Text\\MBF Inat Rem HR.txt"):
    os.remove("Text\\MBF Inat Rem HR.txt")
if os.path.isfile("Text\\MBF Inat Rem MatArras.txt"):
    os.remove("Text\\MBF Inat Rem MatArras.txt")


if test == "0":
    if os.path.isfile("Text\\MB At Emails.csv"):
        os.remove("Text\\MB At Emails.csv")
    if os.path.isfile("Text\\MBF At Emails.csv"):
        os.remove("Text\\MBF At Emails.csv")
    if os.path.isfile("Text\\MB Inat Emails.csv"):
        os.remove("Text\\MB Inat Emails.csv")
    if os.path.isfile("Text\\MBF Inat Emails.csv"):
        os.remove("Text\\MBF Inat Emails.csv")