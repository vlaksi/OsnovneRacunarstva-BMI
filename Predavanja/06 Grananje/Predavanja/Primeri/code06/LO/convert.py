def main():
	c = eval(input("What is the Celsius temperature? "))
	f = 9/5 * c + 32
	print("The temperature is", f, "degrees Fahrenheit.")
	if f>90:
		print("very hot!")
	elif f<30:
		print("very cold!")
	elif f%2!=0:
		print("it is odd out there")
	else:
		print("it is ok out there")
	
main()