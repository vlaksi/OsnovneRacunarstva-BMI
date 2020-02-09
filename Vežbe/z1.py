sep = "|"


def provera_id(id, knjige):
    for knjiga in knjige:
        if knjiga['id'] == id:
            return True
    return False

def kreiraj_knjige(knjige):
    while True:
        knjiga = {}

        knjiga['id'] = input("unesite id: ")
        knjiga['naslov'] = input("unesite nasov: ")
        knjiga['autor'] = input("unesite autora: ")
        knjiga['izdavac'] = input("unesite izdavaca: ")
        knjiga['cena'] = input("unesite cenu: ")
        knjiga['kolicina'] = input("unesite kolicinu: ")
        knjiga['godina_izdavanja'] = input("unesite godinu: ")

        if not provera_id(id, knjige):
            knjige.append(knjiga)
        else:
            print("Id vec postoji!")

        odgovor = input("Da li zelite da nastavite? da/ne")

        if odgovor == "ne":
            break

    f = open("knjige.txt", 'w')

    for knjiga in knjige:
        f.write(knjiga['id'] + sep +
                knjiga['naslov'] + sep +
                knjiga['autor'] + sep +
                knjiga['izdavac'] + sep +
                knjiga['cena'] + sep +
                knjiga['kolicina'] + sep +
                knjiga['godina_izdavanja'] + '\n')


def citanje_knjiga():
    f = open("knjige.txt", 'r')
    knjige = []
    for red in f:
        podaci = red.strip().split(sep)

        knjiga = {}
        knjiga['id'] = podaci[0]
        knjiga['naslov'] = podaci[1]
        knjiga['autor'] = podaci[2]
        knjiga['izdavac'] = podaci[3]
        knjiga['cena'] = podaci[4]
        knjiga['kolicina'] = podaci[5]
        knjiga['godina_izdavanja'] = podaci[6]

        knjige.append(knjiga)

    return knjige

def ispis_knjiga(knjige):
    print("{:<3}{:<30}{:<30}{:<30}{:<30}{:<30}{:<30}".format('id', 'naslov','autori','izdavac','cena','kolicina','godina'))
    print("-"*183)
    for knjiga in knjige:

        print("{:<3}{:<30}{:<30}{:<30}{:<30}{:<30}{:<30}".format(knjiga['id'],
                                      knjiga['naslov'],
                                      knjiga['autor'],
                                      knjiga['izdavac'],
                                      knjiga['cena'],
                                      knjiga['kolicina'],
                                      knjiga['godina_izdavanja']))

    print("-" * 183 + "\n")

def meni():
    knjige = citanje_knjiga()
    while True:
        print("1. Dodaj knjige")
        print("2. Prikazi knjige")
        print("3. Kraj")

        opcija = eval(input("Unesite opciju: "))

        if opcija == 1:
            kreiraj_knjige(knjige)
        elif opcija == 2:
            ispis_knjiga(knjige)
        elif opcija == 3:
            exit()
        else:
            print("Opcija ne postoji!")

meni()