g = 10000
k = 0.08
b_g = 10

def obracun_kredita(glavnica, kamata, broj_godina):
    for i in range(broj_godina):
        glavnica = glavnica+glavnica*kamata
    return glavnica

iznos = obracun_kredita(g,k,b_g)
print(iznos)
print(g)
