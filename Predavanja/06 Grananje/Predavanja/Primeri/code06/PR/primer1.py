import math
def main():
	try:
		a, b, c = eval(input("Please enter the coefficients (a, b, c): "))
		discRoot = math.sqrt(b * b - 4 * a * c)
		root1 = (-b + discRoot) / (2 * a)
		root2 = (-b - discRoot) / (2 * a)
		print("\nThe solutions are:", root1, root2)
	except NameError:
		print("los format podataka")
	except ValueError:
		print("jednacina nema resenja")
	except ZeroDivisionError:
		print("koeficijent a ne moze da bude 0")
	except Exception as e:
		print("nepoznata greska")
		print(e)

main()
