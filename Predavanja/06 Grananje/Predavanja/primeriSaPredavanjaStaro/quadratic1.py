import math
def main():
	try:
		a, b, c = eval(input("Please enter the coefficients (a, b, c): "))
		if b * b - 4 * a * c == 0:
			discRoot = math.sqrt(b * b - 4 * a * c)
			root1 = (-b + discRoot) / (2 * a)
			print("\nThe solution is:", root1)
		else:
			discRoot = math.sqrt(b * b - 4 * a * c)
			root1 = (-b + discRoot) / (2 * a)
			root2 = (-b - discRoot) / (2 * a)
			print("\nThe solutions are:", root1, root2)
	except ValueError as excObj:
	 	if str(excObj)=="math domain error":	 		
	 		print("there are no real roots")
	 	elif str(excObj)=="need more than 2 values to unpack":
	 		print("there should be 3 instead of 2 values")
	 	else:
	 		print(str(excObj))
	except NameError:
	 	print("values should be numbers")
	except:
		print("something went wrong")
main()

