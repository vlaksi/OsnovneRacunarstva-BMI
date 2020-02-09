f = open('brojevi1.csv','r')
red = f.readline()
suma = 0
brojac = 0
while red!='':
    red = red.strip()
    l = red.split(',')
    for ocena in l:
        try:
            suma += float(ocena)
            brojac += 1
        except:
            pass
    red = f.readline()
sr_vrednost = suma / brojac
print(sr_vrednost)
f.close()
