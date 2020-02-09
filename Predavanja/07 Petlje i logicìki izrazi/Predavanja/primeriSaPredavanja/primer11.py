# za dve tacke proveri da li su jednake
p1 = (4, 1, 3) 
p2 = (1.5, 3, 2)
if p1[0] == p2[0]:
    if p1[1] == p2[1]:
        if p1[2] == p2[2]:
            print('tacke su jednake')
        else:
            print('nisu')
    else:
        print('nisu')
else:
    print('nisu')