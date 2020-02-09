f = open('brojevi.csv','r')
s = 0
red = f.readline()
brojac = 0
while red!='':
    brojac += 1
    s += float(red.strip())
    red = f.readline()
sr_vrednost = s/brojac
f.close()
print(sr_vrednost)

