def max1(x1,x2,x3):
	if x1>x2 and x1>x3:
		print(x1)
	elif x2>x1 and x2>x3:
		print(x2)
	else:
		print(x3)

def max2(x1,x2,x3):
	if x1>x2:
		if x1>x3:
			print(x1)
		else:
			print(x3)
	else:
		if x2>x3:
			print(x2)
		else:
			print(x3)

def max3(x1,x2,x3):
	m=x1
	if(x2>m):
		m=x2
	if(x3>m):
		m=x3
	print(m)

def main():
	max1(1,3,2)
	max2(1,3,2)
	max3(1,3,2)

if __name__=="__main__":
	main()
