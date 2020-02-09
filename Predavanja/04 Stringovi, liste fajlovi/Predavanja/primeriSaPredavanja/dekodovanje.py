# 98|108|97 -> bla
kodovani_tekst = input('unesite kodovani tekst:')
dekodovani_tekst = ''
for i in kodovani_tekst.split('|'):
    dekodovani_tekst = dekodovani_tekst + chr(int(i))
print(dekodovani_tekst)