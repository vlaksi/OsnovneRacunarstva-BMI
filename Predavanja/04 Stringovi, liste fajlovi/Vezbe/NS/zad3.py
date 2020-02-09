korisnik=open("korisnik.txt",'a')
korisnicko_ime=raw_input("unesi korisnicko ime:")
lozinka=raw_input("unesi lozinku:")
red=korisnicko_ime+"|"+lozinka+"\n"
korisnik.write(red)
korisnik.close()