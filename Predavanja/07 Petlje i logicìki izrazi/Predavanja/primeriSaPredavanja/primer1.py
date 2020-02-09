# program koji racuna srednju vrednost brojeva iz liste
l = [3,2,5,44,1]
s = 0
for x in l:
    s += x
    # s = s+x
sr_vrednost = s/len(l)
print(sr_vrednost)