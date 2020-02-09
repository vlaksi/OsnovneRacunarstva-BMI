from random import random

def obracun_kredita(glavnice, kamata, broj_godina):
    for i in range(broj_godina):
        for i in range(len(glavnice)):
            glavnice[i] = glavnice[i]+glavnice[i]*kamata*random()
    return glavnice

if __name__ == '__main__':
    g = [10000, 3000, 4000]
    k = 0.08
    b_g = 10
    iznos = obracun_kredita(g,k,b_g)
    print(iznos)
    print(g)
    print('kamata3 name: ',__name__)