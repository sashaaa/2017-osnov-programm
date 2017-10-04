import sys

#read all input
text=sys.stdin.readlines()

sentence_id = 1
#for each line in the text 
for line in text:
	#if the line is blank skip it
	if line.strip() == '':
		continue
	print('# sent_id = %d' % (sentence_id))
	
	sentence_id = sentence_id + 1
	 
	tekst = line
	print('# text = %s' % (tekst))

	punctuation = [".", ",", "!", "?"]
	for mic in punctuation:
			line=line.replace(mic, " "+ mic)
	#to change space for a new line
	texta=line.split (" ")

	#variable to store the token number
	f=1
	
	for b in texta:
		# col:   0                        1       2  3    4      5     6      7     8      9
		print(str(f) + "\t"+ b +" \t_	_	_	_	_	_	_	_")
		f=f+1




