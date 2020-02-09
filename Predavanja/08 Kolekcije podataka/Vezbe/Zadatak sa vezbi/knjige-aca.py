
lista_knjiga = []

def snimi_knjige():
    f = open("knjige.txt", "w")
    for knjiga in lista_knjiga:
        red = str(knjiga["id"])+ "|"
        red += knjiga["naslov"]+ "|"
        red += knjiga["autori"]+ "|"
        red += knjiga["izdavac"]+ "|"
        red += str(knjiga["cena"])+ "|"
        red += str(knjiga["kolicina"])+ "|"
        red += str(knjiga["godina"]) + "\n"
        f.write(red)
    f.close()
    print "="*100        
    print "Uspesno snimanje!"
    print "="*100    
    
    
def ucitaj_knjige():
    f = open("knjige.txt","r")
    for linija in f:
        id,naslov,autori,izdavac,cena,kolicina,godina = linija.strip().split("|")
        dodaj_knjigu(int(id),naslov,autori,izdavac,int(cena),int(kolicina),int(godina))
    f.close()
    print "="*100        
    print "Uspesno ucitavanje!"
    print "="*100    
        
def dodaj_knjigu(id,naslov,autori,izdavac,cena,kolicina,godina):
    knjiga = {}
    knjiga["id"] = id
    knjiga["naslov"] = naslov
    knjiga["autori"] = autori
    knjiga["izdavac"] = izdavac
    knjiga["cena"] = cena
    knjiga["kolicina"] = kolicina
    knjiga["godina"] = godina
    lista_knjiga.append(knjiga)
    
    

def unos_knjige():
    id= int(raw_input("Unesite ID knjige: "))
    naslov = raw_input("Unesite naslov knjige: ")
    autori = raw_input("Unesite autore knjige: ")
    izdavac = raw_input("Unesite izdavaca knjige: ")
    cena = int(raw_input("Unesite cenu knjige: "))
    kolicina = int(raw_input("Unesite kolicinu knjige: "))
    godina = int(raw_input("Unesite godinu knjige: "))
    dodaj_knjigu(id,naslov,autori,izdavac,cena,kolicina,godina)
    
def ispisi_listu():
    header = "id".ljust(5) + "naslov".ljust(15)+ "autori".ljust(20) + "izdavac".ljust(20) + "cena".ljust(10) + "kolicina".ljust(10) + "godina".ljust(10)
    print header
    print "-"*100
    for knjiga in lista_knjiga:
        red = str(knjiga["id"]).ljust(5)
        red += knjiga["naslov"].ljust(15)
        red += knjiga["autori"].ljust(20)
        red += knjiga["izdavac"].ljust(20)
        red += str(knjiga["cena"]).ljust(10)
        red += str(knjiga["kolicina"]).ljust(10) 
        red += str(knjiga["godina"]).ljust(10)
        print red
        
choice = ""
print "SISTEM ZA EVIDENTIRANJE KNJIGA"
print "-"*100
while choice != "5":
    choice = ""
    print "\nOdaberite opciju:"
    print "1) Dodaj knjigu"
    print "2) Izlistaj knjige"
    print "3) Ucitaj knjige"
    print "4) Sacuvaj knjige"
    print "5) Kraj rada"
    choice = raw_input("> ")
    if choice == "1":
        unos_knjige()
    elif choice == "2":
        ispisi_listu()
    elif choice == "3":
        ucitaj_knjige()
    elif choice == "4":
        snimi_knjige()
    elif choice == "5":
        print "="*100        
        print "Dovidjenja!"
        print "="*100
    else:
        print "Nepostojeca opcija!"

    

    