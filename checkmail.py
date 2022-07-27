import csv
from html.parser import HTMLParser
import os

class MyHTMLParser(HTMLParser):
	counter = 0

	def handle_data(self, data):
		if self.counter == 3:
			check = 0
			if mode == 1:
				femails = open("Text\\MB At Emails.csv", "r",encoding='utf8')
			elif mode == 2:
				femails = open("Text\\MBF At Emails.csv", "r",encoding='utf8')
			elif mode == 3:
				femails = open("Text\\MB Inat Emails.csv", "r",encoding='utf8')
			elif mode == 4:
				femails = open("Text\\MBF Inat Emails.csv", "r",encoding='utf8')
			reader = csv.reader(femails,delimiter=',')
			data = data.strip()
			for row in reader:
				if data == row[0]:
					check = 1
					break
			if check == 0:
				print(data)
			femails.close()
			self.counter = -1
		elif self.counter == 2 and data[0] == 'l' and data[1] == 'u' and data[2] == 'n' and data[3] == 'o' and data[4] == '(' and data[5] == 'a' and data[6] == ')':
			self.counter = 3
		elif self.counter == 1 and data[0] == 'A' and data[1] == 't' and data[2] == 'é' and data[3] == ' ' and data[4] == 'o':
			self.counter = 2
		elif self.counter == 0 and data[0] == 'P' and data[1] == 'r' and data[2] == 'e' and data[3] == 'z' and data[4] == 'a' and data[5] == 'd' and data[6] == 'o':
			self.counter = 1

#MB AT
if os.path.isfile("Text\\new.txt"):
    os.remove("Text\\new.txt")
mode = 1
fbody = open("Text\\MB At.txt", "r",encoding='utf8')
f2 = open("Text\\new.txt", "w",encoding='utf8')
reader = fbody.read()
reader = reader.replace("<br></div></div>", "<br></div></div>\n")
reader = reader.replace("\n</body>", "")
reader = reader.replace("<div style=\"page-break-after:always\"><br><br><span style=\"font-size:13px\">", "<div style=\"page-break-after:always\"><span style=\"font-size:13px\">")
reader = reader.replace("<body contenteditable=\"true\" class=\"cke_editable cke_editable_themed cke_contents_ltr cke_show_borders\" spellcheck=\"false\" style=\"cursor: auto;\">", "")
f2.write(reader)
fbody.close()
f2.close()
f2 = open("Text\\new.txt", "r",encoding='utf8')
print("MB At")
for line in f2:
    parser = MyHTMLParser()
    parser.feed(line)
f2.close()

#MBF AT
if os.path.isfile("new.txt"):
    os.remove("new.txt")
mode = 2
fbody = open("Text\\MBF At.txt", "r",encoding='utf8')
f2 = open("Text\\new.txt", "w",encoding='utf8')
reader = fbody.read()
reader = reader.replace("<br></div></div>", "<br></div></div>\n")
reader = reader.replace("\n</body>", "")
reader = reader.replace("<div style=\"page-break-after:always\"><br><br><span style=\"font-size:13px\">", "<div style=\"page-break-after:always\"><span style=\"font-size:13px\">")
reader = reader.replace("<body contenteditable=\"true\" class=\"cke_editable cke_editable_themed cke_contents_ltr cke_show_borders\" spellcheck=\"false\" style=\"cursor: auto;\">", "")
f2.write(reader)
fbody.close()
f2.close()
f2 = open("Text\\new.txt", "r",encoding='utf8')
print("MBF At")
for line in f2:
    parser = MyHTMLParser()
    parser.feed(line)
f2.close()

#MB INAT
if os.path.isfile("new.txt"):
    os.remove("new.txt")
mode = 3
fbody = open("Text\\MB Inat.txt", "r",encoding='utf8')
f2 = open("Text\\new.txt", "w",encoding='utf8')
reader = fbody.read()
reader = reader.replace("<br></div></div>", "<br></div></div>\n")
reader = reader.replace("\n</body>", "")
reader = reader.replace("<div style=\"page-break-after:always\"><br><br><span style=\"font-size:13px\">", "<div style=\"page-break-after:always\"><span style=\"font-size:13px\">")
reader = reader.replace("<body contenteditable=\"true\" class=\"cke_editable cke_editable_themed cke_contents_ltr cke_show_borders\" spellcheck=\"false\" style=\"cursor: auto;\">", "")
f2.write(reader)
fbody.close()
f2.close()
f2 = open("Text\\new.txt", "r",encoding='utf8')
print("MB Inat")
for line in f2:
    parser = MyHTMLParser()
    parser.feed(line)
f2.close()

#MBF INAT
if os.path.isfile("new.txt"):
    os.remove("new.txt")
mode = 4
fbody = open("Text\\MBF Inat.txt", "r",encoding='utf8')
f2 = open("Text\\new.txt", "w",encoding='utf8')
reader = fbody.read()
reader = reader.replace("<br></div></div>", "<br></div></div>\n")
reader = reader.replace("\n</body>", "")
reader = reader.replace("<div style=\"page-break-after:always\"><br><br><span style=\"font-size:13px\">", "<div style=\"page-break-after:always\"><span style=\"font-size:13px\">")
reader = reader.replace("<body contenteditable=\"true\" class=\"cke_editable cke_editable_themed cke_contents_ltr cke_show_borders\" spellcheck=\"false\" style=\"cursor: auto;\">", "")
f2.write(reader)
fbody.close()
f2.close()
f2 = open("Text\\new.txt", "r",encoding='utf8')
print("MBF Inat")
for line in f2:
    parser = MyHTMLParser()
    parser.feed(line)
f2.close()

#INFANTIL
path = "Infantil\\"
files = os.listdir(path)
print("Infantil")
for f in files:
	femails = open("Text\\MB At Emails.csv", "r",encoding='utf8')
	reader = csv.reader(femails,delimiter=',')
	check = 0
	name = f.split('.')
	for row in reader:
		if name[0] == row[0]:
			check = 1
			break
	if check == 0:
		print(name[0])
	femails.close()

#FUNDAMENTAL
path = "Fundamental\\1\\"
files = os.listdir(path)
print("Fundamental")
#FUNDAMENTAL FOLDER 1
for f in files:
	femails = open("Text\\MBF At Emails.csv", "r",encoding='utf8')
	reader = csv.reader(femails,delimiter=',')
	check = 0
	name = f.split('.')
	if name[0][len(name[0])-1] == '1' or name[0][len(name[0])-1] == '2' or name[0][len(name[0])-1] == '3':
		aluno = name[0][:-1]
		for row in reader:
			if aluno == row[0]:
				check = 1
				break
		if check == 0:
			print(aluno)
	femails.close()

path = "Fundamental\\2\\"
files = os.listdir(path)
#FUNDAMENTAL FOLDER 2
for f in files:
	femails = open("Text\\MBF At Emails.csv", "r",encoding='utf8')
	reader = csv.reader(femails,delimiter=',')
	check = 0
	name = f.split('.')
	if name[0][len(name[0])-1] == '1':
		aluno = name[0][:-1]
		for row in reader:
			if aluno == row[0]:
				check = 1
				break
		if check == 0:
			print(aluno)
	femails.close()

path = "Fundamental\\3\\"
files = os.listdir(path)
#FUNDAMENTAL FOLDER 3
for f in files:
	femails = open("Text\\MBF At Emails.csv", "r",encoding='utf8')
	reader = csv.reader(femails,delimiter=',')
	check = 0
	name = f.split('.')
	if name[0][len(name[0])-1] == '1':
		aluno = name[0][:-1]
		for row in reader:
			if aluno == row[0]:
				check = 1
				break
		if check == 0:
			print(aluno)
	femails.close()