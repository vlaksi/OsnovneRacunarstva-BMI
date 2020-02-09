def dodaj(lista,knjiga):
    for i in lista:
        if i["id"]==knjiga["id"]:
            return False
    lista.append(knjiga)
    return True

def prikazi(lista):
    print "id  naslov  autor  izdavac  cena  kolicina  godina"
    print "--------------------------------------------------"
    for knjiga in lista:
        print str(knjiga["id"]).ljust(4)+knjiga["naslov"][:7].ljust(8)+knjiga["autor"][:6].ljust(7)+knjiga["izdavac"][:8].ljust(9)+str(knjiga["cena"])[:5].ljust(6)+str(knjiga["kolicina"])[:9].ljust(10)+str(knjiga["godina"])[:7].ljust(8)
lista=[]

def unesiKnjigu():
    knjiga = {}
    ident = raw_input("Unesite id knjige>>")
    knjiga['id']=ident
    naziv = raw_input("Unesite naziv knjige>>")
    knjiga['naslov']=naziv
    autor = raw_input("Unesite naziv autora>>")
    knjiga['autor']=autor
    izdavac = raw_input("Unesite izdavaca>>")
    knjiga['izdavac']=izdavac
    cena = raw_input("Cena>>")
    knjiga['cena']=cena
    kolicina = raw_input("Kolicina>>")
    knjiga['kolicina']=kolicina
    godina = raw_input("Godina izdavanja>>")
    knjiga['godina']=godina

    return knjiga     

def knjiga2Str(knjiga):
    s = str(knjiga["id"])+"|"+knjiga["naslov"]+"|"+knjiga["autor"]+"|"+str(knjiga["cena"])+"|"+str(knjiga["kolicina"])+"|"+str(knjiga["godina"])+"|"+knjiga['izdavac']
    return s

def str2Knjiga(red):
    knjiga = {}
    deo = red.strip().split("|")
    knjiga["id"] = int(deo[0])
    knjiga["naslov"] = deo[1]
    knjiga["autor"] = deo[2]
    knjiga['kolicina'] = int(deo[3])
    knjiga["cena"] = int(deo[4])
    knjiga['godina'] = int(deo[5])
    knjiga['izdavac'] = deo[6]
    return knjiga

def snimi(lista, putanja):
    fajl=open(putanja,"w")
    for knjiga in lista:
        fajl.write(knjiga2Str(knjiga)+'\n')
    fajl.close()
    #za svaku knjigu u listi 
        #snimi u fajl red
        #id|naslov|autor...
    

def ucitaj(putanja):
    fajl=open(putanja,"r")
    l=[]
    for red in fajl.readlines():
        l.append(str2Knjiga(red))
    fajl.close()
    return l

        
if __name__=="__main__":
    dodaj(lista,{"id":1,"naslov":"zelena milja","autor":"Stiven King","izdavac":"prometej","kolicina":4,"cena":1800,"godina":2004})
    dodaj(lista,{"id":2,"naslov":"homo sacer","autor":"Djordjo Agamben","izdavac":"svetlost","kolicina":8,"cena":700,"godina":2013})
    dodaj(lista,{"id":3,"naslov":"u odbranu izgubljenih ciljeva","autor":"Slavoj Zizek","izdavac":"plato","kolicina":10,"cena":2700,"godina":2010})
    print lista
    prikazi(lista)
    print knjiga2Str(lista[1])
    print str2Knjiga("2|homo sacer|Djordjo Agamben|700|8|2013|adsfdafs")
    snimi(lista,"knjiga.txt")
    print ucitaj("knjiga.txt")


