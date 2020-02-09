def kamata(x):
	kamata = 0.1
	x = x + x*kamata
	print("osnovica u funkciji: ",x)
	return x

osnovica = 10000
o = kamata(osnovica)
print("osnovica vracena iz funkcije: ",o)
print("osnovica posle funkcije: ",osnovica)

print("******************************************")

def kamata_sa_listama(x):
	kamata = 0.1
	x[0] = x[0] + x[0]*kamata
	print("osnovica u funkciji: ",x[0])
	return x

osnovica = [10000]
o = kamata_sa_listama(osnovica)
print("osnovica vracena iz funkcije: ",o[0])
print("osnovica posle funkcije: ",osnovica[0])