import sys

text=sys.stdin.read()

texta=text.replace('z. B. ', 'b1&')
textb=texta.replace('. ', '. \n')
textc=textb.replace('b1&', 'z. B. ')

print(textc)   