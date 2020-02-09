# napisati program u kome korisnik unosi niz fraza odvojenih zarezom. Program zatim upisuje sve unete fraze u datoteku fraze.txt tako da je svaka fraza u zasebnom redu

fraze = input('unesi fraze: ')
# fraze = 'asdf asdf, afdsa fdas fdsa, asdf dfs sdaf'
fraze = fraze.split(',')
f_out = open('fraze.txt','w')
for fraza in fraze:
    print(fraza.strip(),file=f_out)
f_out.close()