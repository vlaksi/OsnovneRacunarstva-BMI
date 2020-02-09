def prebrojReci(listaReci):
	d = {}
	for rec in listaReci:
		if rec in d.keys():
			d[rec]+=1
		else:
			d[rec]=1
	return d

def fileToListaReci():
	tekstF = open("tekst.txt","r")
	tekst = tekstF.read()
	tekstF.close()
	for ch in "!\"#$%&()*+,-./:;<=>?@[\\]^_’{|}":
		tekst = tekst.replace(ch, " ")
	retVal = tekst.split()
	return retVal

def reciKey(par):
	return par[1]

def main():
	listaReci = fileToListaReci()
	reci = prebrojReci(listaReci).items()
	reci = list(reci)
	#reci.sort(key=reciKey, reverse=True)
	reci.sort(key=lambda x: x[1], reverse=True)
	print(reci)

main()
