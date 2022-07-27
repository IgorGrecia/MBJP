import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import csv
from html.parser import HTMLParser
import os
import timeit

test = input('Real = 0\nTest = 1\n')

class MyHTMLParser(HTMLParser):
    counter = 0
    signature = "<div id=\":ot\" class=\"Am aiL IP Al editable Xp0HJf-LW-avf\" hidefocus=\"true\" aria-label=\"Assinatura\" g_editable=\"true\" role=\"textbox\" aria-multiline=\"true\" contenteditable=\"true\" style=\"direction: ltr;\"><font color=\"#cc0000\"><b><div><br></div>Igor Lúcio</b></font><br><div><b>Auxiliar Administrativo</b></div><div>+55 (83) 3224-8910<br></div><div><a href=\"http://maplebear.com.br/joao-pessoa\" target=\"_blank\">maplebear.com.br/joaopessoa</a></div><div><img src=\"https://ci4.googleusercontent.com/proxy/eLsTgrS3ey04sehfXmvFG2gPqJfXxNbAn-NreJ1vaX40jLcra4Dq8CCrtn-RxdRnY1nXtu2G3kYnn2QsRFjHtXTY746nVuZ2ORpUHi6UFo-gs-NWh_axG7K08Gs9B7KqNtA8=s0-d-e1-ft#https://drive.google.com/uc?id=1BC44jfmCzwpppQP-IPqLYFT4HkcMDhF_&export=download\" alt=\"maple.jpg\" width=\"452\" height=\"84\"></div></div>"
    if test == "0":
        password = input('Password\n')
        if password != "real":
            print("Wrong Password\n")
            sys.exit()
        print("Password OK\n")
        sender_address = 'igor.lucio@maplebear.com.br'
        sender_pass = 'cucsbfgicykornmh'
    elif test == "1":
        sender_address = 'igorgreciapython@gmail.com'
        sender_pass = 'gfcncsywvlwuypvl'

    def handle_data(self, data):
        if self.counter == 2:
            receiver_address = ""
            if school == 1:
                femails = open("Text\\MB At Emails.csv", "r",encoding='utf8')
            elif school == 2:
                femails = open("Text\\MBF At Emails.csv", "r",encoding='utf8')
            reader = csv.reader(femails,delimiter=',')
            data = data.strip()
            for row in reader:
                if data == row[0]:
                    receiver_address = row[1]+","+row[2]+","+row[3]
                    break
            if receiver_address == "":
                if school == 1:
                    femails = open("Text\\MB Inat Emails.csv", "r",encoding='utf8')
                elif school == 2:
                    femails = open("Text\\MBF Inat Emails.csv", "r",encoding='utf8')
                reader = csv.reader(femails,delimiter=',')
                data = data.strip()
                for row in reader:
                    if data == row[0]:
                        receiver_address = row[1]+","+row[2]+","+row[3]
                        break
            if test == "0":
                html = """<html><body>"""+line+self.signature+"""</body></html>"""
            elif test == "1":
                html = """<html><body>"""+receiver_address+line+self.signature+"""</body></html>"""
            msg = MIMEMultipart()
            msg['From'] = self.sender_address
            if test == "0":
                msg['To'] = receiver_address
            elif test == "1":
                msg['To'] = 'igorgreciapython@gmail.com'
            msg['Subject'] = 'Maple Bear - Biblioteca'   #The subject line
            msg.attach(MIMEText(html, 'html'))
            s = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
            s.starttls() #enable security
            s.login(self.sender_address, self.sender_pass) #login with mail_id and password
            if test == "0":
                s.sendmail(self.sender_address, receiver_address.split(','), msg.as_string())
            elif test == "1":
                s.sendmail(self.sender_address, 'igorgreciapython@gmail.com', msg.as_string())
            s.quit()
            femails.close()
            self.counter = -1
        if self.counter == 1 and data[0] == 'N' and data[1] == 'o' and data[2] == 's' and data[3] == 's' and data[4] == 'o':
            self.counter = 2
        if self.counter == 0 and data[0] == 'P' and data[1] == 'r' and data[2] == 'e' and data[3] == 'z' and data[4] == 'a' and data[5] == 'd' and data[6] == 'o':
            self.counter = 1

start = timeit.default_timer()

#MB
school = 1
fbody = open("Text\\HR MB Fixed.txt", "r",encoding='utf8')
for line in fbody:
    parser = MyHTMLParser()
    parser.feed(line)
fbody.close()

#MBF
school = 2
fbody = open("Text\\HR MBF Fixed.txt", "r",encoding='utf8')
for line in fbody:
    parser = MyHTMLParser()
    parser.feed(line)
fbody.close()

stop = timeit.default_timer()
print('Time: ', stop - start) 