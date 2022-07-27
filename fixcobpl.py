from html.parser import HTMLParser
import os

def add_zero(n):
    k = str(n)
    c = 0
    for element in k:
        if c > 0:
            c += 1
        if element == '.':
            c = 1
    if c == 2:
        k = k.ljust(1 + len(k), '0')
    return k


class MyHTMLParser(HTMLParser):
    start = 0
    multa = ""
    data_counter = 0
    value = 0
    value_j = 0

    def handle_data(self, data):
        global val
        global valj
        global tot
        global totj
        if self.data_counter == -2:
            totj = float(data.replace(",", "."))
            self.data_counter = 0
        if self.data_counter == -1:
            self.data_counter-=1
            tot = float(data.replace(",", "."))
        if self.data_counter == 4:
            self.data_counter = 0
            self.value_j += float(data.replace(",", "."))
            valj = self.value_j
        elif self.data_counter == 3:
            k = data.replace(",", ".")
            self.value += float(k)
            val = self.value
        if self.data_counter > 0:
            self.data_counter+=1
        if data == "Multa - Home Reading":
            self.data_counter = 1
            self.multa = data
        elif data == "Camiseta":
            self.data_counter = 1
            self.multa = data
        elif data == "Matific App":
            self.data_counter = 1
            self.multa = data
        elif data == "Perda de Livro - Home Reading":
            self.data_counter = 1
            self.multa = data
        elif data == "Total:":
            self.data_counter = -1

    def handle_starttag(self, tag, attrs):
        if tag == "tr":
            self.start = self.getpos()[1]

    def handle_endtag(self, tag):
        global end
        global line
        global sta
        if tag == "tr" and self.multa == "Multa - Home Reading":
            end.append(self.getpos()[1]+5)
            sta.append(self.start)
            self.multa = ""
        elif tag == "tr" and self.multa == "Camiseta":
            end.append(self.getpos()[1]+5)
            sta.append(self.start)
            self.multa = ""
        elif tag == "tr" and self.multa == "Matific App":
            end.append(self.getpos()[1]+5)
            sta.append(self.start)
            self.multa = ""
        elif tag == "tr" and self.multa == "Perda de Livro - Home Reading":
            end.append(self.getpos()[1]+5)
            sta.append(self.start)
            self.multa = ""

#MB At
if os.path.isfile("Text\\new.txt"):
    os.remove("Text\\new.txt")
fbody = open("Text\\MB At.txt", "r",encoding='utf8')
if os.path.isfile("Text\\MB At Rem MatArras.txt"):
    os.remove("Text\\MB At Rem MatArras.txt")
f3 = open("Text\\MB At Rem MatArras.txt", "w",encoding='utf8')
f2 = open("Text\\new.txt", "w",encoding='utf8')
reader = fbody.read()
reader = reader.replace("<br></div></div>", "<br></div></div>\n")
reader = reader.replace("\n</body>", "")
reader = reader.replace("<div style=\"page-break-after:always\"><br><br>", "<div style=\"page-break-after:always\">")
reader = reader.replace("<body contenteditable=\"true\" class=\"cke_editable cke_editable_themed cke_contents_ltr cke_show_borders\" spellcheck=\"false\" style=\"cursor: auto;\">", "")
f2.write(reader)
fbody.close()
f2.close()
f2 = open("Text\\new.txt", "r",encoding='utf8')
for line in f2:
    val = 0
    valj = 0
    tot = 0
    totj = 0
    idx = 0
    end = []
    end.append(0)
    sta = []
    parser = MyHTMLParser()
    parser.feed(line)
    if val > 0:
        if tot - val == 0:
            continue
        for idx, v in enumerate(sta):
            f3.write(line[int(end[idx]):int(sta[idx])])
        idx+=1
        line = line.replace(str(add_zero(tot)).replace(".",","),str(add_zero(tot - val)).replace(".",","))
        line = line.replace(str(add_zero(totj)).replace(".",","),str(add_zero(round(totj - valj,2))).replace(".",","))
    f3.write(line[int(end[idx]):])
f2.close()
f3.close()

#MB Inat
if os.path.isfile("Text\\new.txt"):
    os.remove("Text\\new.txt")
fbody = open("Text\\MB Inat.txt", "r",encoding='utf8')
if os.path.isfile("Text\\MB Inat Rem MatArras.txt"):
    os.remove("Text\\MB Inat Rem MatArras.txt")
f3 = open("Text\\MB Inat Rem MatArras.txt", "w",encoding='utf8')
f2 = open("Text\\new.txt", "w",encoding='utf8')
reader = fbody.read()
reader = reader.replace("<br></div></div>", "<br></div></div>\n")
reader = reader.replace("\n</body>", "")
reader = reader.replace("<div style=\"page-break-after:always\"><br><br>", "<div style=\"page-break-after:always\">")
reader = reader.replace("<body contenteditable=\"true\" class=\"cke_editable cke_editable_themed cke_contents_ltr cke_show_borders\" spellcheck=\"false\" style=\"cursor: auto;\">", "")
f2.write(reader)
fbody.close()
f2.close()
f2 = open("Text\\new.txt", "r",encoding='utf8')
for line in f2:
    val = 0
    valj = 0
    tot = 0
    totj = 0
    idx = 0
    end = []
    end.append(0)
    sta = []
    parser = MyHTMLParser()
    parser.feed(line)
    if val > 0:
        if tot - val == 0:
            continue
        for idx, v in enumerate(sta):
            f3.write(line[int(end[idx]):int(sta[idx])])
        idx+=1
        line = line.replace(str(add_zero(tot)).replace(".",","),str(add_zero(tot - val)).replace(".",","))
        line = line.replace(str(add_zero(totj)).replace(".",","),str(add_zero(round(totj - valj,2))).replace(".",","))
    f3.write(line[int(end[idx]):])
f2.close()
f3.close()

#MBF At
if os.path.isfile("Text\\new.txt"):
    os.remove("Text\\new.txt")
fbody = open("Text\\MBF At.txt", "r",encoding='utf8')
if os.path.isfile("Text\\MBF At Rem MatArras.txt"):
    os.remove("Text\\MBF At Rem MatArras.txt")
f3 = open("Text\\MBF At Rem MatArras.txt", "w",encoding='utf8')
f2 = open("Text\\new.txt", "w",encoding='utf8')
reader = fbody.read()
reader = reader.replace("<br></div></div>", "<br></div></div>\n")
reader = reader.replace("\n</body>", "")
reader = reader.replace("<div style=\"page-break-after:always\"><br><br>", "<div style=\"page-break-after:always\">")
reader = reader.replace("<body contenteditable=\"true\" class=\"cke_editable cke_editable_themed cke_contents_ltr cke_show_borders\" spellcheck=\"false\" style=\"cursor: auto;\">", "")
f2.write(reader)
fbody.close()
f2.close()
f2 = open("Text\\new.txt", "r",encoding='utf8')
for line in f2:
    val = 0
    valj = 0
    tot = 0
    totj = 0
    idx = 0
    end = []
    end.append(0)
    sta = []
    parser = MyHTMLParser()
    parser.feed(line)
    if val > 0:
        if tot - val == 0:
            continue
        for idx, v in enumerate(sta):
            f3.write(line[int(end[idx]):int(sta[idx])])
        idx+=1
        line = line.replace(str(add_zero(tot)).replace(".",","),str(add_zero(tot - val)).replace(".",","))
        line = line.replace(str(add_zero(totj)).replace(".",","),str(add_zero(round(totj - valj,2))).replace(".",","))
    f3.write(line[int(end[idx]):])
f2.close()
f3.close()

#MBF Inat
if os.path.isfile("Text\\new.txt"):
    os.remove("Text\\new.txt")
fbody = open("Text\\MBF Inat.txt", "r",encoding='utf8')
if os.path.isfile("Text\\MBF Inat Rem MatArras.txt"):
    os.remove("Text\\MBF Inat Rem MatArras.txt")
f3 = open("Text\\MBF Inat Rem MatArras.txt", "w",encoding='utf8')
f2 = open("Text\\new.txt", "w",encoding='utf8')
reader = fbody.read()
reader = reader.replace("<br></div></div>", "<br></div></div>\n")
reader = reader.replace("\n</body>", "")
reader = reader.replace("<div style=\"page-break-after:always\"><br><br>", "<div style=\"page-break-after:always\">")
reader = reader.replace("<body contenteditable=\"true\" class=\"cke_editable cke_editable_themed cke_contents_ltr cke_show_borders\" spellcheck=\"false\" style=\"cursor: auto;\">", "")
f2.write(reader)
fbody.close()
f2.close()
f2 = open("Text\\new.txt", "r",encoding='utf8')
for line in f2:
    val = 0
    valj = 0
    tot = 0
    totj = 0
    idx = 0
    end = []
    end.append(0)
    sta = []
    parser = MyHTMLParser()
    parser.feed(line)
    if val > 0:
        if tot - val == 0:
            continue
        for idx, v in enumerate(sta):
            f3.write(line[int(end[idx]):int(sta[idx])])
        idx+=1
        line = line.replace(str(add_zero(tot)).replace(".",","),str(add_zero(tot - val)).replace(".",","))
        line = line.replace(str(add_zero(totj)).replace(".",","),str(add_zero(round(totj - valj,2))).replace(".",","))
    f3.write(line[int(end[idx]):])
f2.close()
f3.close()