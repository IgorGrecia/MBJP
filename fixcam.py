from html.parser import HTMLParser
import os

class MyHTMLParser(HTMLParser):
    data_counter = 0
    start = 0
    value_counter = 0
    loop_start = 15
    multa = ""

    def handle_data(self, data):
        if self.value_counter == 1 and data.isnumeric() == True:
            self.value_counter = 0
        else:
            self.value_counter = 0
            self.data_counter+=1
            self.multa = data
            if data == "Valor":
                self.value_counter = 1

    def handle_starttag(self, tag, attrs):
        if self.data_counter==self.loop_start-1:
            self.start = self.getpos()[1]

    def handle_endtag(self, tag):
        global end
        global line
        global f3
        if self.data_counter==self.loop_start:
            if self.multa[0] == 'M' and self.multa[1] == 'u' and self.multa[2] == 'l' and self.multa[3] == 't' and self.multa[4] == 'a':
                self.loop_start+=1
            else:
                f3.write(line[int(end):int(self.start)])
                end=self.getpos()[1]+5
                self.loop_start+=3

#MB
if os.path.isfile("Text\\new.txt"):
    os.remove("Text\\new.txt")
fbody = open("Text\\Cam MB.txt", "r",encoding='utf8')
if os.path.isfile("Text\\Cam MB Fixed.txt"):
    os.remove("Text\\Cam MB Fixed.txt")
f3 = open("Text\\Cam MB Fixed.txt", "a",encoding='utf8')
f2 = open("Text\\new.txt", "w",encoding='utf8')
reader = fbody.read()
reader = reader.replace("<br></div></div>", "<br></div></div>\n")
reader = reader.replace("\n</body>", "")
reader = reader.replace("<br><br><br>", "")
reader = reader.replace("<div style=\"page-break-after:always\"><br>","<div style=\"page-break-after:always\">")
reader = reader.replace("<body contenteditable=\"true\" class=\"cke_editable cke_editable_themed cke_contents_ltr cke_show_borders\" spellcheck=\"false\">", "")
reader = reader.replace("<td style=\"text-align:center; width:50px\"><strong>Qtd Dias</strong></td>", "")
reader = reader.replace("<td style=\"text-align:right\"><strong>Valor com Juros</strong></td>", "")
reader = reader.replace("<td style=\"text-align:center; width:50px\"><br></td>", "")
reader = reader.replace("Nosso sistema gerou o valor abaixo ap??s identificar a devolu????o de livros emprestados para ", "N??o identificamos em nosso sistema a quita????o da camisa do Maple Bear Games 2021 d")
reader = reader.replace(" fora do prazo previsto (at?? quinta-feira ap??s o empr??stimo).", ".")
reader = reader.replace("O valor poder?? ser quitado", "O valor poder?? ser quitado na recep????o da escola (cr??dito, d??bito ou dinheiro) ou")
reader = reader.replace(", por favor desconsiderar a mensagem. Em caso de diverg??ncia das informa????es acima, por favor encaminhar mensagem para a Biblioteca atrav??s da agenda TellMe.", " e para facilitar o controle, pode ser enviado o comprovante em resposta a este e-mail")
reader = reader.replace("<em>Lembramos que o nosso programa<strong>&nbsp;Home Reading</strong>&nbsp;continua gratuito, como tamb??m prolongamos a data da devolu????o do livro da segunda-feira ap??s o empr??stimo para at?? a quinta-feira ap??s o empr??stimo. Pedimos sempre que seja observado o prazo de devolu????o, colaborando para que outras crian??as possam ter acesso aos exemplares numa pr??xima data de empr??stimo.</em>", "")
reader = reader.replace("<br><br><br><br>", "<br><br>")
f2.write(reader)
fbody.close()
f2.close()
f2 = open("Text\\new.txt", "r",encoding='utf8')
for line in f2:
    end = 0
    parser = MyHTMLParser()
    parser.feed(line)
    f3.write(line[int(end):])
f2.close()
f3.close()

#MBF
if os.path.isfile("Text\\new.txt"):
    os.remove("Text\\new.txt")
fbody = open("Text\\Cam MBF.txt", "r",encoding='utf8')
if os.path.isfile("Text\\Cam MBF Fixed.txt"):
    os.remove("Text\\Cam MBF Fixed.txt")
f3 = open("Text\\Cam MBF Fixed.txt", "a",encoding='utf8')
f2 = open("Text\\new.txt", "w",encoding='utf8')
reader = fbody.read()
reader = reader.replace("<br></div></div>", "<br></div></div>\n")
reader = reader.replace("\n</body>", "")
reader = reader.replace("<br><br><br>", "")
reader = reader.replace("<div style=\"page-break-after:always\"><br>","<div style=\"page-break-after:always\">")
reader = reader.replace("<body contenteditable=\"true\" class=\"cke_editable cke_editable_themed cke_contents_ltr cke_show_borders\" spellcheck=\"false\">", "")
reader = reader.replace("<td style=\"text-align:center; width:50px\"><strong>Qtd Dias</strong></td>", "")
reader = reader.replace("<td style=\"text-align:right\"><strong>Valor com Juros</strong></td>", "")
reader = reader.replace("<td style=\"text-align:center; width:50px\"><br></td>", "")
reader = reader.replace("Nosso sistema gerou o valor abaixo ap??s identificar a devolu????o de livros emprestados para ", "N??o identificamos em nosso sistema a quita????o da camisa do Maple Bear Games 2021 d")
reader = reader.replace(" fora do prazo previsto (at?? quinta-feira ap??s o empr??stimo).", ".")
reader = reader.replace("O valor poder?? ser quitado", "O valor poder?? ser quitado na recep????o da escola (cr??dito, d??bito ou dinheiro) ou")
reader = reader.replace(", por favor desconsiderar a mensagem. Em caso de diverg??ncia das informa????es acima, por favor encaminhar mensagem para a Biblioteca atrav??s da agenda TellMe.", " e para facilitar o controle, pode ser enviado o comprovante em resposta a este e-mail")
reader = reader.replace("<em>Lembramos que o nosso programa<strong>&nbsp;Home Reading</strong>&nbsp;continua gratuito, como tamb??m prolongamos a data da devolu????o do livro da segunda-feira ap??s o empr??stimo para at?? a quinta-feira ap??s o empr??stimo. Pedimos sempre que seja observado o prazo de devolu????o, colaborando para que outras crian??as possam ter acesso aos exemplares numa pr??xima data de empr??stimo.</em>", "")
reader = reader.replace("<br><br><br><br>", "<br><br>")
f2.write(reader)
fbody.close()
f2.close()
f2 = open("Text\\new.txt", "r",encoding='utf8')
for line in f2:
    end = 0
    parser = MyHTMLParser()
    parser.feed(line)
    f3.write(line[int(end):])
f2.close()
f3.close()