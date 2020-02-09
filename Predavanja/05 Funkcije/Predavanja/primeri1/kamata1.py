glavnica = 10000
kamata = 0.08
broj_godina = 10

for i in range(broj_godina):
    glavnica = glavnica+glavnica*kamata

print(glavnica)