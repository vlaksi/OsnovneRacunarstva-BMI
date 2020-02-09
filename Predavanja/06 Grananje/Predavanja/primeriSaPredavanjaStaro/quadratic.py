import math
def main():
	sa_tastature = input("Please enter the coefficients (a, b, c): ")
	if len(sa_tastature.split(",")) !=3 :
		print("there must be exactly 3 values: ")
	#a, b, c = eval(input("Please enter the coefficients (a, b, c): "))
	#print("sa_tastature:",sa_tastature)
	a, b, c = eval(sa_tastature)
	if b * b - 4 * a * c < 0:
		print("There are no real roots")

	# else:
	# 	discRoot = math.sqrt(b * b - 4 * a * c)
	# 	root1 = (-b + discRoot) / (2 * a)
	# 	if b * b - 4 * a * c == 0:
	# 		print("\nThe solution is:", root1)	
	# 	else:
	# 		root2 = (-b - discRoot) / (2 * a)
	# 		print("\nThe solutions are:", root1, root2)

	elif b * b - 4 * a * c == 0:
		discRoot = math.sqrt(b * b - 4 * a * c)
		root1 = (-b + discRoot) / (2 * a)
		print("\nThe solution is:", root1)
	else:
		discRoot = math.sqrt(b * b - 4 * a * c)
		root1 = (-b + discRoot) / (2 * a)
		root2 = (-b - discRoot) / (2 * a)
		print("\nThe solutions are:", root1, root2)

main()