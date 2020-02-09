import math
def main():
	a, b, c = eval(input("Please enter the coefficients (a, b, c): "))
	try:
		disc = b * b - 4 * a * c 
		discRoot = math.sqrt(disc)
		root1 = (-b + discRoot) / (2 * a)
		root2 = (-b - discRoot) / (2 * a)
		print("\nThe solutions are:", root1, root2)
	except ValueError:
		print("There are no real solutions")
	except ZeroDivisionError:
		print("a must not be 0")
main()