def min1(x1,x2,x3):
	if x1<x2:
		if x1<x3:
			return x1
	if x2<x1:
		if x2<x3:
			return x2
	if x3<x1:
		if x3<x2:
			return x3

def min2(x1,x2,x3):
	if x1<x2 and x1<x3:
		return x1
	if x2<x1 and x2<x3:
		return x2
	if x3<x1 and x3<x2:
		return x3

def min3(l):
	temp=l[0]
	for x in l:
		if x<temp:
			temp=x
	return temp


if __name__=="__main__":
	x = min([2,3,1])
	print(x)