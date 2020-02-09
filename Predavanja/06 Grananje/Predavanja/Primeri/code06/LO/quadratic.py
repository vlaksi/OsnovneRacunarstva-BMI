# quadratic.py
import math
def main():
	try:
		a, b, c = eval(input("Please enter the coefficients (a, b, c): "))
		if b * b - 4 * a * c > 0:
			discRoot = math.sqrt(b * b - 4 * a * c)
			root1 = (-b + discRoot) / (2 * a)
			root2 = (-b - discRoot) / (2 * a)
			print("\nThe solutions are:", root1, root2)
		elif b * b - 4 * a * c == 0:
			discRoot = math.sqrt(b * b - 4 * a * c)
			root = (-b + discRoot) / (2 * a)
			print("\nThe solution is:", root)
		else:
			print("\nThe function does not have real roots!")
	except NameError:
		print("\nThe input values were wrong!")
	except ValueError as e:
		print("\nThe number of input values was wrong!")
		print("\nError message was:\n")
		print(str(e))
main()