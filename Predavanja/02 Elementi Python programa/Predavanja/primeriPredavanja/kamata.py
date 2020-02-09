kamata = eval(input('kamata u %: '))
broj_meseci = eval(input('broj meseci: '))
dugovanje = eval(input('dugovanje: '))
for i in range(broj_meseci):
    dugovanje = dugovanje + dugovanje*kamata/100
print('dugovanje',dugovanje)
