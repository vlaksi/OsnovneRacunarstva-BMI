def equal_points(a, b):
	if a[0]==b[0]:
		if a[1]==b[1]:
			if a[2]==b[2]:
				return True
			else:
				return False	
		else:
			return False
	else:
		return False

def equal_points_1(a, b):
	if a[0]==b[0] and a[1]==b[1] and a[2]==b[2]:
		return True
	else:
		return False	


def main():
	a=(1,1,1)
	b=(0,0,0)
	print(equal_points_1(a,b))
	# a=(1,1)
	# b=(0,1)
	# print(equal_points(a,b))
	# a=(1,1)
	# b=(1,0)
	# print(equal_points(a,b))
	# a=(0,0)
	# b=(0,0)
	# print(equal_points(a,b))


if __name__ == '__main__':
	main()