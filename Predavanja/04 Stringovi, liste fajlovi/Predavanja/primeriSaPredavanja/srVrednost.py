f_in = open('podaci.csv','r')
redovi = f_in.readlines()
f_in.close()
suma = 0
for red in redovi:
    suma = suma + float(red)
sr_vrednost = suma/len(redovi)
print(sr_vrednost)