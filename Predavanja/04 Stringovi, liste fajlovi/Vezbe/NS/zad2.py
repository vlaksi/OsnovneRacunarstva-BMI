string = raw_input('Unesite frazu : ')
string = string.title()
l = string.split(' ')
akronim = ''
for i in l:
	akronim += i[0]
print(akronim)