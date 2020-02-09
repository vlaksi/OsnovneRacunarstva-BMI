def kvadrat(x):
    ret_val = x**2
    return ret_val

def koren(x):
    pocetak = 0
    kraj = x
    for i in range(1000):
        sredina = (pocetak + kraj) / 2
        kv = sredina * sredina
        if kv == x:
            return kv
        elif kv > x:
            kraj = sredina
        else:
            pocetak = sredina
    return sredina
