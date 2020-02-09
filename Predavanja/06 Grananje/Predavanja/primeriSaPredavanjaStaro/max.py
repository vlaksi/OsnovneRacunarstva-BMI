def max_1(x,y,z):
	if x>y and x>z:
		return x
	if y>x and y>z:
		return y
	if z>x and z>y:
		return z

def max_2(x,y,z):
	if x>y:
		if x>z:
			return x
		else:
			return z
	else:
		if y>z:
			return y
		else:
			return z

def max_3(x,y,z):
	maks=x
	if y>maks:
		maks=y
	if z>maks:
		maks=z
	return maks

def max_4(niz):
	maks = niz[0]
	for x in niz:
		if x>maks:
			maks=x
	return maks

def max_5(*args):
	maks = args[0]
	for x in args:
		if x>maks:
			maks=x
	return maks

def max_6(*args, maks, i):
	if args[i]>maks:
		maks = args[i]
	i+=1
	if i>= len(args):
		return maks
	else:
		return max_6(*args, maks=maks, i=i)

def max_7(*args):
	return max_6(*args, maks=args[0], i=0)

def max_8(*args):
	return max(*args)

def main():
	x=2
	y=1
	z=3
	# m = max_4([2,3,1])
	m = max_8(x,y,z)
	print(m)

main()