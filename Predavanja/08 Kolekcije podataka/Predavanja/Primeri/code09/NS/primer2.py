def prebrojReci():
	tekstF = open("tekst.txt","r")
	tekst = tekstF.read()
	tekst = tekst.lower()
	for ch in "!\"#$%&()*+,-./:;<=>?@[\\]^_’{|}":
		tekst = tekst.replace(ch, " ")
	d = {}
	reci = tekst.split()
	for rec in reci:
		if rec in d:
			d[rec]+=1
		else:
			d[rec]=1
	return d

def keyF(s):
	return s[1]

def main():
	d = prebrojReci()
	lista = list(d.items())
	#lista.sort(key=keyF, reverse=True)
	lista.sort(key=lambda x: x[1], reverse=True)
	print(lista)

main()