def min1(x1,x2,x3):
	if x1<x2:
		if x1<x3:
			return x1
		else:
			return x3
	elif x2<x3:
		return x2
	else:
		return x3

def min2(l):
	m=l[0]
	for x in l:
		if x<m:
			m=x
	return m

m = min1(2,1,3)
print(m)
m = min2([2,1,3])
print(m)

