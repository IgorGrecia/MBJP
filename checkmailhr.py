import csv
from html.parser import HTMLParser
import os

class MyHTMLParser(HTMLParser):
    counter = 0

    def handle_data(self, data):
        if self.counter == 2:
            check = 0
            if mode == 1:
                femails = open("Text\\MB At Emails.csv", "r",encoding='utf8')
            elif mode == 2:
                femails = open("Text\\MBF At Emails.csv", "r",encoding='utf8')
            reader = csv.reader(femails,delimiter=',')
            data = data.strip()
            for row in reader:
                if data == row[0]:
                    check = 1
                    break
            if check == 0:
                if mode == 1:
                    femails = open("Text\\MB Inat Emails.csv", "r",encoding='utf8')
                elif mode == 2:
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
        if self.counter == 1 and data[0] == 'N' and data[1] == 'o' and data[2] == 's' and data[3] == 's' and data[4] == 'o':
            self.counter = 2
        if self.counter == 0 and data[0] == 'P' and data[1] == 'r' and data[2] == 'e' and data[3] == 'z' and data[4] == 'a' and data[5] == 'd' and data[6] == 'o':
            self.counter = 1

#MB HR
fbody = open("Text\\HR MB Fixed.txt", "r",encoding='utf8')
mode = 1
print("MB HR")
for line in fbody:
    parser = MyHTMLParser()
    parser.feed(line)
fbody.close()

#MBF HR
fbody = open("Text\\HR MBF Fixed.txt", "r",encoding='utf8')
mode = 2
print("MBF HR")
for line in fbody:
    parser = MyHTMLParser()
    parser.feed(line)
fbody.close()