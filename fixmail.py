import os

for i in range(4):
	if i == 0:
		em="Text\\MB At Emails.csv"
	if i == 1:
		em="Text\\MBF At Emails.csv"
	if i == 2:
		em="Text\\MB Inat Emails.csv"
	if i == 3:
		em="Text\\MBF Inat Emails.csv"

	fbody = open(em, "r",encoding='utf8')
	reader = fbody.read()
	fbody.close()
	reader = reader.replace(" ,", ",")
	reader = reader.strip()
	reader = reader.replace('Milena Góes Barbosa Gaudêncio,delanogaudencio@magshopping.com.br', 'Milena Góes Barbosa Gaudêncio,targino@magshopping.com.br', 1)
	reader = reader.replace('Ana Carolina Bianchi Vieira,bellinha.mbianchi@gmail.com', 'Ana Carolina Bianchi Vieira,clinepa200@gmail.com', 1)
	reader = reader.replace('Carlos Henrique Teixeira Gadelha de Sá,luan_gadelha_7@hotmail.com', 'Carlos Henrique Teixeira Gadelha de Sá,lojasbugary@gmail.com', 1)
	reader = reader.replace('Luís Felipe Pinto Cavalcanti,felipe@ftcrepresentacoes.com.br', 'Luís Felipe Pinto Cavalcanti,contasapagar@redmobile.com.br', 1)
	reader = reader.replace('Marina Pinto Cavalcanti,felipe@ftcrepresentacoes.com.br', 'Marina Pinto Cavalcanti,contasapagar@redmobile.com.br', 1)
	reader = reader.replace('Laís Paiva de Assis,elmo.assis@grupoelfa.com.br', 'Laís Paiva de Assis,elisangela.naressi@hsns.com.br', 1)
	reader = reader.replace('Liz Paiva de Assis,elmo.assis@grupoelfa.com.br', 'Liz Paiva de Assis,elisangela.naressi@hsns.com.br', 1)
	reader = reader.replace('Luma Paiva de Assis,elmo.assis@grupoelfa.com.br', 'Luma Paiva de Assis,elisangela.naressi@hsns.com.br', 1)
	reader = reader.replace('ricawerner@gmail.com', '')
	reader = reader.replace('rosa.pamplona@hotmail.com', '')
	reader = reader.replace('marcellafabricio@gmail.com', '')
	reader = reader.replace('centrodeneurocirurgia@hotmail.com', '')
	reader = reader.replace('Ana Rachel Granville Ximenes,rachel_granville@hotmail.com,rachel_granville@hotmail.com,rachel_granville@hotmail.com','Ana Rachel Granville Ximenes,rachel_granville@hotmail.com,rachel_granville@hotmail.com,construtoramashia@hotmail.com')
	reader = reader.replace('Maria Alves Guedes Pereira,janainajapiassu@gmail.com,gcgp@histo.com.br,janainajapiassu@gmail.com', 'Maria Alves Guedes Pereira,janainajapiassu@gmail.com,,')
	reader = reader.replace('Diva Alves Guedes Pereira,gcgp@histo.com.br,gcgp@histo.com.br,janainajapiassu@gmail.com', 'Diva Alves Guedes Pereira,gcgp@histo.com.br,,')
	reader = reader.replace('anaflaviavelloso@uol.com.br,erick@erickmacedo.adv.br,anaflaviavelloso@uol.com.br', 'financeiro@erickmacedo.adv.br,erick@erickmacedo.adv.br,anaflaviavelloso@uol.com.br')
	reader = reader.replace('contato@barbaraveiga.com.br,robertofflopes@hotmail.com,contato@barbaraveiga.com.br', 'contato@barbaraveiga.com.br,robertofflopes@hotmail.com,nebiaraujo@yahoo.com.br')
	reader = reader.replace('Alice Ferreira Ribeiro,,,\n', '')
	fbody = open(em, "w",encoding='utf8')
	fbody.write(reader)
	fbody.close()