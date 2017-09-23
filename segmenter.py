import sys

text=sys.stdin.read()

texta=text.replace('с. ш. ', '&')
textb=texta.replace ('з. д. ', '@')
textc=textb.replace('. ', '. \n')
textd=textc.replace('&', 'с. ш. ')
texte=textd.replace('@', 'с. д. ')

print(texte)   