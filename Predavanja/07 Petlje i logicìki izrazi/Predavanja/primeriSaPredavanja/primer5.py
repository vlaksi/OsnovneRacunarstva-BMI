# sentinel petlja
s = 0
brojac = 0
broj = float(input('unesi broj (-5 za kraj): '))
while broj!=-5:
    s += broj
    brojac += 1
    broj = float(input('unesi broj (-5 za kraj): '))
sr_vrednost = s/brojac
print(sr_vrednost)