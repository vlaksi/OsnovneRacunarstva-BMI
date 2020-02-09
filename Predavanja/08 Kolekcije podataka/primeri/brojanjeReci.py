def get_word_count(item):
	return item[1]

def brojanje_reci():
	f = open("tekst.txt","r")
	tekst = f.read()
	f.close()
	tekst = tekst.lower()
	for ch in "!\"#$%&()*+,-./:;<=>?@[\\]^_’{|}":
		tekst = tekst.replace(ch,"")
	words = tekst.split(" ")
	d = {}
	for word in words:
		if word in d:
			d[word] += 1
		else:
			d[word] = 1
	items = list(d.items())
	print(sorted(items, key = get_word_count, reverse=True))

def main():
	brojanje_reci()

if __name__ == '__main__':
	main()