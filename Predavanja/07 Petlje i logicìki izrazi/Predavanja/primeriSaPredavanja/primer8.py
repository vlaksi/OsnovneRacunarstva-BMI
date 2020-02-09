# break
s = 0
brojac = 0
while True:
    unos = input('unesi broj (prazno za kraj): ')
    if unos=='':
        break
    s += float(unos)
    brojac += 1
sr_vrednost = s/brojac
print(sr_vrednost)