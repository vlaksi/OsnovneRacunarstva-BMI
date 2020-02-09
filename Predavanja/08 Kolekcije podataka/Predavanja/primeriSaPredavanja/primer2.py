def srednja_vrednost(l):
    return sum(l)/len(l)

def ucitaj_podatke():
    l = []
    xStr = input("Unesite broj (<Enter> za kraj) >> ")
    while xStr != "":
        x = eval(xStr)
        l.append(x)
        xStr = input("Unesite broj (<Enter> za kraj) >> ")
    return l

def ucitaj_podatke_iz_fajla(naziv_fajla):
    pass
# TODO uraditi za domaci

def median(l):
    l.sort()
    if len(l)%2 != 0:
        return l[len(l)//2]
    else:
        return (l[len(l)//2] + l[len(l)//2-1])/2

def st_dev(l):
    sr_vrednost = srednja_vrednost(l)
    s = 0
    for x in l:
        s += (sr_vrednost - x)**2
    return (s/(len(l)-1))**(1/2)

def main():
    l = ucitaj_podatke()
    print('srednja vrednost: ', srednja_vrednost(l))
    print('median: ',median(l))
    print('standardna devijacija: ',st_dev(l))

main()

