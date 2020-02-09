def replaceInterpunction(tekst):
	for ch in "!\"#$%&()*+,-./:;<=>?@[\\]^_’{|}":
		tekst = tekst.replace(ch, " ")
	return tekst

def compareWords(p):
	return p[1]

def main():
	f = open("tekst.txt", "r")
	tekst = f.read()
	tekst = replaceInterpunction(tekst)
	tekst = tekst.lower()
	print(tekst)
	reci = tekst.split()
	ponavljanja = {}
	for rec in reci:
		if rec in ponavljanja:
			ponavljanja[rec]+=1
		else:
			ponavljanja[rec]=1
	ponavljanjaL = list(ponavljanja.items())
	#ponavljanjaL.sort(key=lambda x: x[1], reverse=True)
	ponavljanjaL.sort(key=compareWords, reverse=True)
	print(ponavljanjaL)

main()