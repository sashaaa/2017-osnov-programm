
import sys
 
text = sys.stdin.readlines()
 	 
 	 
def latinizator(letter, dic):
 	for j, i in dic.items():
 		letter = letter.replace(i, j)
 	return letter

legend = {

"a":"а",
"э":"ä",
"ай":"ai",
"э":"e",
 "э":"é",
"ай":"ei",
 "éi":"ай",
"эу":"ё",
"и":"i",
"о":"o",
"эу":"ou",
"у":"u",
"уэ":"ue",
"б":"b",
"к":"c",
"кс":"ch",
"д":"d",
"ф":"f",
"г":"g",
"х":"h",
"й":"j",
"к":"k",
"л":"l",
"м":"m",
"н":"n",
"н":"ng",
"п":"p",
"к":"q",
"р":"r",
"с":"s",
"ш":"sch",
"шп":"sp",
"шт":"st",
"т":"t",
"ф":"v",
"в":"w",
"з":"x",
"й":"y",
"тс":"z",

"А":"A",
"Э":"Ä",
"И":"I",
"О":"O",
"У":"U",
"Б":"B",
"К":"C",
"Д":"D",
"Ф":"F",
"Г":"G",
"Х":"H",
"Й":"J",
"К":"K",
"Л":"L",
"М":"M",
"Н":"N",
"П":"P",
"К":"Q",
"Р":"R",
"С":"S",
"Ш":"Sch",
"Шп":"Sp",
"Шт":"St",
"Т":"T",
"Ф":"V",
"В":"W",
"З":"X",
"Й":"Y",
"Тс":"Z",
}


for line in text:
	if line.strip() == '':
		continue

	if '\t' not in line:
		print(line.strip())
		continue
 	 
	texta=line.split ("\t")
 	 
	f=1
 	 
	token = texta[1]
	texta[9] = latinizator(token, legend)
	print('\t'.join(texta))