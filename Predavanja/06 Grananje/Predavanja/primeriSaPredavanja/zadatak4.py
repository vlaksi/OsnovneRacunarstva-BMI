# unose se dva stringa. program ispisuje poslednja 4 slova prvog i prvo slovo drugog ponovljeno 5 puta. prvo slovo novog stringa mora da bude veliko, ostala mala
s1 = input('s1: ')
s2 = input('s2: ')
za_ispis = s1[-4].upper()+s1[-3:].lower()+5*s2[0].lower()
print(za_ispis)