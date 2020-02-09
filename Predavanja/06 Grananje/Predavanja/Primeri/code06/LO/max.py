def max1(x1,x2,x3):
	if x1>x2 and x1>x3:
		return x1
	elif x2>x1 and x2>x3:
		return x2
	else:
		return x3

def max2(x1,x2,x3):
	if x1>x2:
		if x1>x3:
			return x1
		else:
			return x3
	else:
		if x2>x3:
			return x2
		else:
			return x3
			
def max3(x1,x2,x3):
	m = x1
	if x2>m:
		m=x2
	if x3>m:
		m=x3
	return m
	
def maxL(l):
	m = l[0]
	for x in l:
		if x > m:
			m = x
	return m

if __name__=="__main__":	
	x = max1(1,3,2)
	print(x)
	x = max2(1,3,2)
	print(x)
	x = max3(1,3,2)
	print(x)
	x = maxL([1,3,2,5,4,2])
	print(x)
	x=max(1,3,2)
	print(x)