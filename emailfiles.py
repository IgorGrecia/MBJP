import os

if os.path.isfile("C:\\Users\\igorb\\Downloads\\Maple Bear Alunos - MB At Emails.csv"):
	os.rename("C:\\Users\\igorb\\Downloads\\Maple Bear Alunos - MB At Emails.csv", 'Text\\MB At Emails.csv')
if os.path.isfile("C:\\Users\\igorb\\Downloads\\Maple Bear Alunos - MB Inat Emails.csv"):
	os.rename('C:\\Users\\igorb\\Downloads\\Maple Bear Alunos - MB Inat Emails.csv', 'Text\\MB Inat Emails.csv')
if os.path.isfile("C:\\Users\\igorb\\Downloads\\Maple Bear Alunos - MBF At Emails.csv"):
	os.rename('C:\\Users\\igorb\\Downloads\\Maple Bear Alunos - MBF At Emails.csv', 'Text\\MBF At Emails.csv')
if os.path.isfile("C:\\Users\\igorb\\Downloads\\Maple Bear Alunos - MBF Inat Emails.csv"):
	os.rename('C:\\Users\\igorb\\Downloads\\Maple Bear Alunos - MBF Inat Emails.csv', 'Text\\MBF Inat Emails.csv')