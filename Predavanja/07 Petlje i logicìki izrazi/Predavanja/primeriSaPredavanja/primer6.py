# sentinel petlja
s = 0
brojac = 0
unos = input('unesi broj (prazno za kraj): ')
while unos!='':
    s += float(unos)
    brojac += 1
    unos = input('unesi broj (prazno za kraj): ')
sr_vrednost = s/brojac
print(sr_vrednost)