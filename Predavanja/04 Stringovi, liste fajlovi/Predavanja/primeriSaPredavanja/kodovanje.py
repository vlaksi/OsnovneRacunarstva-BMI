tekst = input("Unesite tekst: ")
rezultat = "" 
for i in tekst:
  rezultat = rezultat + str(ord(i)) + '|'
  
print(rezultat[:-1])
