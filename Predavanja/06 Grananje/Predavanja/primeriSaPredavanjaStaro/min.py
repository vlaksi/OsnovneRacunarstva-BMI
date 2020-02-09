def min1(x,y,z):
	if x<y and x<z:
		return x
	if y<x and y<z:
		return y
	if z<x and z<y:
		return z

def min2(x,y,z):
	if x<y:
		if x<z:
			return x
		else:
			return z
	else:
		if y<z:
			return y
		else:
			return z

def min3(x,y,z):
	ret_val = x
	if y<ret_val:
		ret_val = y
	if z<ret_val:
		ret_val = z

def min4(*args):
	ret_val = args[0]
	for i in range(1,len(args)):
		if args[i]<ret_val:
			ret_val = args[i]
	return ret_val

def min5(*args):
	return min(args)

def min6(*args,ret_val,i):
	if args[i]<ret_val:
		ret_val = args[i]
	i += 1
	if i<len(args):
		ret_val = min6(*args,ret_val=ret_val,i=i)
	return ret_val

def main():
	x = 2
	y = 1
	z = 3
	print(min1(x,y,z))
	print(min2(x,y,z))
	print(min6(x,y,z,ret_val=x, i=0))

if __name__ == '__main__':
	main()
	