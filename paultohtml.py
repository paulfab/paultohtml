# -*- coding: utf-8 -*-

import sys


def create_template(elements):
	try:
		fichier_name = elements[1]
	except IndexError :
		print("The file to be translated is not indicated")
		exit()
	try:
		fichier = open(fichier_name, 'r')
	except:
		print("Impossible to open the file : " + fichier_name)
		exit()

	nb_lang = len(elements) -2
	if nb_lang <1 :
		print("Please use at least two languages")
		exit()
	
	list_lang = []
	for i in elements[2:]:
		list_lang.append(i)
	
	print("The document is going to be translated in : " + str(list_lang))

	file_lang = {}

	for lang in list_lang:
		file_lang[lang] = open(fichier_name[:fichier_name.rfind(".")]+"_"+lang+".html", "w")


	content = fichier.read()

	for lang in list_lang:
		index_p = 0
		index_n = 0
		while index_n != -1:
			index_p = index_n
			index_n = content.find("<%%%", index_p)
			if index_n == -1 :
				file_lang[lang].write(content[index_p:])
				break

			file_lang[lang].write(content[index_p:index_n])
			blank = content.find("%%%"+lang, index_n) 
			last = content.find("%%%>", index_n)

			next_o = content.find("<%%%",index_n +1)
			if last == -1 or (next_o != -1 and ( next_o < last)):
				ligne = "L" +str(content.count("\n",0,index_n) +1) + " "
				print(ligne + "Tag never closed: " + content[index_n: index_n + 30].replace("\n",""))
				exit()


			if blank != -1 and blank  < last:
				blank = blank + 3 + len(lang)
				fin_sequence = content.find("%%%", blank )
				file_lang[lang].write(content[blank:fin_sequence].strip())
			else :
				ligne = "L" +str(content.count("\n",0,index_n) +1) + " "
				print(ligne+ "Missing " + lang + " translation : "+ content[index_n: index_n + 30].replace("\n","") )
			index_n = last+4

		file_lang[lang].close()

	fichier.close()

if __name__ == '__main__':
	create_template(sys.argv)

