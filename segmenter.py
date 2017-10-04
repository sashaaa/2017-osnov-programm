import sys

text=sys.stdin.readlines()

for line in text:
	texta=line.replace('z. B. ', 'b1&')
	textb=texta.replace('. ', '. \n')
	textc=textb.replace('b1&', 'z. B. ')

	print(textc)   