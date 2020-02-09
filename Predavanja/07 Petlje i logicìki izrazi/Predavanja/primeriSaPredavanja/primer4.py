# program koji racuna srednju vrednost brojeva dok god korisnik ne odluci da prekine unos brojeva
s = 0
dalje = 'da'
brojac = 0
while dalje=='da':
    brojac += 1
    broj = float(input('unesi broj: '))
    s += broj
    dalje = input('dalje? ')
sr_vrednost = s/brojac
print(sr_vrednost)