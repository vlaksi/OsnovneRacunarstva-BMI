redniBroj = eval(input("redni broj meseca: "))
meseci = "JanFebMarAprMajJunJulAvgSepOktNovDec"
mesec = meseci[(redniBroj-1)*3:(redniBroj-1)*3+3]
print(mesec)