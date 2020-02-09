import math
def main():
	try:
		a, b, c = eval(input("Please enter the coefficients (a, b, c): "))
		d = b * b - 4 * a * c
		if d>0:
			discRoot = math.sqrt(b * b - 4 * a * c)
			root1 = (-b + discRoot) / (2 * a)
			root2 = (-b - discRoot) / (2 * a)
			print("\nThe solutions are:", root1, root2)
		elif d==0:
			x = -b/(2*a)
			print("resenje je:", x)	
		else:
			print("jednacina nema realnih resenja")	
	except NameError:
		print("Vrednosti moraju da budu brojevi")
	except ZeroDivisionError:
		print("Parametar a ne sme da bude 0")
	except Exception as e:
		print("Nesto nije u redu")
		print(e)
main()