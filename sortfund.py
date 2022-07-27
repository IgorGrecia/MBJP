import os
from os.path import join, isfile

path = "Fundamental\\"
if os.path.isdir(path+"1") == False:
	os.mkdir(path+"1")
if os.path.isdir(path+"2") == False:
	os.mkdir(path+"2")
if os.path.isdir(path+"3") == False:
	os.mkdir(path+"3")

files = [f for f in os.listdir(path) if isfile(join(path, f)) and f[len(f)-5] == '3']
for f in files:
	aluno = f[:-5]
	newf=aluno+"1"+".pdf"
	os.rename(path+newf, path+"3\\"+newf)
	newf=aluno+"2"+".pdf"
	os.rename(path+newf, path+"3\\"+newf)
	newf=aluno+"3"+".pdf"
	os.rename(path+newf, path+"3\\"+newf)

files = [f for f in os.listdir(path) if isfile(join(path, f)) and f[len(f)-5] == '2']
for f in files:
	aluno = f[:-5]
	newf=aluno+"1"+".pdf"
	os.rename(path+newf, path+"2\\"+newf)
	newf=aluno+"2"+".pdf"
	os.rename(path+newf, path+"2\\"+newf)

files = [f for f in os.listdir(path) if isfile(join(path, f)) and f[len(f)-5] == '1']
for f in files:
	aluno = f[:-5]
	newf=aluno+"1"+".pdf"
	os.rename(path+newf, path+"1\\"+newf)