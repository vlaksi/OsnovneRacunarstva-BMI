# program koji racuna prosecnu vrednost brojeva koje korisnik unosi sa tastature
broj_brojeva = int(input('unesi broj brojeva: '))
s = 0
for i in range(broj_brojeva):
    x = float(input('unesi broj: '))
    s += x
sr_vrednost = s / broj_brojeva
print(sr_vrednost)