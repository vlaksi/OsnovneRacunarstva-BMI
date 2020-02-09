korisnici = open('korisnici.txt', 'r')
for line in korisnici:
    print('koriscniko ime:' + line.strip().split("|")[0])
    print('lozinka:' + line.strip().split("|")[1])
korisnici.close()