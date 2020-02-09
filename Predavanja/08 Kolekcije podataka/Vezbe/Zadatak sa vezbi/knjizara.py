import knjige

def prikaziMeni():
    print "1) listanje knjiga"
    print "2) dodavanje knjige"
    print "3) izlaz"

def main():
    lKnjige=knjige.ucitaj("knjiga.txt")    
    while True:
        prikaziMeni()   
        izbor=raw_input(">> ")
        if izbor=="1":
            knjige.prikazi(lKnjige)            
        elif izbor=="2":
            k=knjige.unesiKnjigu()
            uspesnoDodavanje=knjige.dodaj(lKnjige,k) 
            if uspesnoDodavanje:
                knjige.snimi(lKnjige, "knjiga.txt")
                print "knjiga je uspesno dodata"
            else:
                print "vec postoji knjiga sa tim identifikatorom"        
        elif izbor=="3":
            print "dovidjenja"
            break
        else:
            print "komanda nije prepoznata" 

if __name__=="__main__":
    main()
