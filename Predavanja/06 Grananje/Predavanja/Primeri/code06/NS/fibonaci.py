def fibonaci(n):
	a=1
	b=1
	for i in range(n-2):
		a,b=b,a+b
	return b
