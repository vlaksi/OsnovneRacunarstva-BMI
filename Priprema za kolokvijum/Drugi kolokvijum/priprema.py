"""
Zadaci za pripremu drugog kolokvijuma iz Osnova racunarstva [ BMI ] 2019/20

Vladislav.
"""

"""
Zadatak 1.

Sekvenca sirakuza se racuna pocevsi od prirodnog broja x kao:
    x_sledece:
            - ako je x_trenutno parno:      x_trenutno/2
            - ako je x_trenutno neparno:    3*x_trenutno + 1

Napisati funkciju koja prima inicijalnu vrednost x i vraca listu sa Sirakuza
sekvencom za tu vrednost.
"""
def sirakuza(prosledjeni_broj):
    sirakuza_lista = [prosledjeni_broj]                 # Sirakuza se sastoji od prosledjenog broja i sledecih novoformiranih.
    broj = prosledjeni_broj
    while broj != 1:                                    # Posto sirakuza smanjuje broj dok nije 1, imamo while petlju koja to cini.
        if broj % 2 == 0:                               # U slucaju da je broj PARAN: [ Podsetnik: moduo tj. % je ostatak pri deljenju ]
            broj = broj / 2
        else:                                           # U slucaju da je broj NEPARAN
            broj = 3 * broj +1

        sirakuza_lista.append(broj)                     # Na nasu sirakuza listu dodajemo novi broj.
    return sirakuza_lista

"""
Zadatak 2.

Napisati program koji korisniku omogucava da prvo kaze koliko reci zeli da unese,
nakon cega unosi taj broj reci i ispisuje rec koja je najvise puta unesena.

Ukoliko postoji vise reci sa istim brojem ponavljanja vratiti prvu na koju naidje.
"""
def zadatak2():                                         # funkcija bez parametara
    lista_unetih_reci = []                              # Lista u kojoj cuvamo unete reci
    lista_brojac_reci = []                              # Lista koja broji koliko se puta data rec ponovila

    print("Unesite broj reci koji zelite uneti:")
    br_reci = int(input())                              # Posto input uzima ono sto korisnik unese, a to je tipa string
    while br_reci != 0:                                 # neophodno je to prebaciti u tipa broja tj. int da bi s njim dalje radili
        print("Unesite rec: ")
        unesena_rec = input()
        if unesena_rec not in lista_unetih_reci:        # Ako unete rec nije u listi unetih reci, dodamo je, i kazemo da je to njeno
            lista_unetih_reci.append(unesena_rec)       # prvo pojavljivanje ( dodamo 1 u listu_brojaca_reci )
            lista_brojac_reci.append(1)
        else:                                           # A ako se ta rec vec pojavljivala, povecamo broj njenih pojavljivanja
            index_reci = lista_unetih_reci.index(unesena_rec)
            lista_brojac_reci[index_reci] += 1

        br_reci -= 1                                    # Prelazimo na novu iteraciju

    max_element = max(lista_brojac_reci)                # Izvlacimo ko se najvise puta pojavljivao i onda ga ispisujemo
    index_max_elementa = lista_brojac_reci.index(max_element)
    print("Rec sa najvecim brojem unosa je: " + lista_unetih_reci[index_max_elementa])


"""
Zadatak 3.

Data je datoteka sa programerima strukture id|ime|prezime|oblast|satnica

Napisati funkciju "filtriraj" koja prima putanju do datoteke, string i dva broja
na osnovu kojih se vrsi pretraga.

Funkcija vraca listu programera cija oblast sadrzi zadati string i satnica se nalazi
izmedju dva uneta broja.

"""
def filtriraj(putanja, oblast, granica1, granica2):
    fajl = open(putanja,"r")                                # OTVARANJE FAJLA
    lista_programera = []                                   # Povratna lista iz funkcije u kojoj se nalaze programeri
                                                            # koji zadovljavaju prosledjene kriterijume.

    #lista_programera['id'] = nesto
    for linija_fajla in fajl:                               # Prolazimo kroz svaku liniju u fajlu
        splitovan_niz = linija_fajla.strip().split("|")     # strip uradimo kako bi dobili samo reci, a split da bi dobili reci bez | ( delimiter )
        if oblast in splitovan_niz[3]:                      # Ako su oblast i granice uredu, vrsimo dodavanje u nasu listu programera
            if granica1 <= int(splitovan_niz[4]) and granica2 >= int(splitovan_niz[4]):
                element = {}
                element['id'] = splitovan_niz[0]
                element['ime'] = splitovan_niz[1]
                element['prezime'] = splitovan_niz[2]
                element['oblast'] = splitovan_niz[3]
                element['satnica'] = splitovan_niz[4]
                lista_programera.append(element)

    fajl.close()                                            # ZATVARANJE FAJLA - OBAVEZNO !!
    return lista_programera

"""
Zadatak 4.

Napisati program koji omogucava izmenu satnice radnicima iz datoteke zadate u
trecem zadatku.

"""
def izmenaSatnice():
    print("Unesite id programera: ")
    id = input()
    print("Unesite novu satnicu: ")
    nova_satnica = input()

    # Kada smo dobili podatke, nadjemo tog programera i izmenimo mu satnicu.
    fajl = open("programeri.txt", "r+")                     # OTVARANJE - u rezimu r+ kako bih mogao menjati fajl

    linije = fajl.readlines()
    j = 0                                                   # Index u kojoj smo liniji trenutno.
    for linija in linije:                                   # Prolazim kroz svaku liniju teksta i splitujem je.
        splitovan_niz = linija.strip().split("|")
        if splitovan_niz[0] == id:                          # Ako imamo programera sa tim id-em, menjamo mu satnicu
            splitovan_niz[4] = nova_satnica
            lajna = ""                                      # Pravimo novu liniju kako bi izmeni sadrzaj fajla
            i = 0
            for i in range(len(splitovan_niz)):             # Prolazim kroz citav splitovan niz
                lajna += splitovan_niz[i]                   # i pravim string tipa id|ime|prezime|oblast|satnica
                if i == (len(splitovan_niz) - 1):           # Ako smo dosli pred kraj, nemoj | staviti nego novi red
                    lajna += "\n"
                else:
                    lajna += "|"

            linije[j] = lajna                               # Posto imamo index u kojoj smo liniji, tu celu niju izmenimo
        j += 1
    fajl.close()                                            # ZATVARANJE FAJLA - OBAVEZNO !

    fajl = open("programeri.txt","w+")                      # OTVARANJE - u DRUGOM REZIMU - rezim PISANJA u fajl
    fajl.writelines(linije)                                 # Upisivanje linija u fajl.
    fajl.close()                                            # ZATVARANJE FAJLA - OBAVEZNO !


"""
Zadatak 5.

Napisati program koji za dati niz brojeva racuna njihovu prosecnu vrednost, a zatim
ispisuje ukupan broj clanova niza koji su veci i ukupan broj clanova koji su manji
od prosecne vrednosti.

Program takodje treba da ispise broj iz niza koji ima najblizu vrednost prosecnoj
vrednosti.

"""
def odnos_proseka(niz_brojeva):
    print(niz_brojeva)
    suma = 0
    for broj in niz_brojeva:
        suma += broj
    prosek = suma / len(niz_brojeva)
    # print("prosek: " + str(prosek))

    manjih = 0
    vecih = 0
    najblizi = prosek + 22                          # cisto da nije skroz isti kao najblizi nego malo pomeren od njega
    for broj in niz_brojeva:
        if broj < prosek:
            manjih += 1
        elif broj > prosek:
            vecih += 1

        if abs(broj-prosek) < abs(najblizi - prosek):
            najblizi = broj

    print("Manjih od proseka ima " + str(manjih))
    print("Vecih od proseka ima " + str(vecih))
    print("Najbliza vrednost proseku " + str(najblizi))

"""
Main naseg programa, u kome vrsimo testiranje nasih zadataka.
"""
if __name__ == "__main__":
    # Test zadatka 1
    print("-------------------------------- ZADATAK 1 --------------------------------")
    print(sirakuza(5))
    print("---------------------------------------------------------------------------\n")


    # Test zadatka 2
    print("-------------------------------- ZADATAK 2 --------------------------------")
    zadatak2()
    print("---------------------------------------------------------------------------\n")


    # Test zadatka 3
    print("-------------------------------- ZADATAK 3 --------------------------------")
    print(filtriraj("programeri.txt", "web", 10, 25))
    print("---------------------------------------------------------------------------\n")


    # Test zadatka 4
    print("-------------------------------- ZADATAK 4 --------------------------------")
    izmenaSatnice()
    print("---------------------------------------------------------------------------\n")


    # Test zadatka 5
    print("-------------------------------- ZADATAK 5 --------------------------------")
    odnos_proseka([4, 9, 1, 32, 13])
    print("\n")
    odnos_proseka([4, 8, 12, 16, 14, 18])
    print("---------------------------------------------------------------------------\n")














