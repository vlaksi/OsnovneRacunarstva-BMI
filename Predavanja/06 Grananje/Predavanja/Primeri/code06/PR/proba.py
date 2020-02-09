x = 2
try:
	x = 3
	print(x)
	x = a
except NameError:
	print("greska")
print(x)