def main():
	c = eval(input("What is the Celsius temperature? "))
	f = 9/5 * c + 32
	print("The temperature is", f, "degrees Fahrenheit.")
	if f>90:
		print("it's very hot out there!")
	if f<30:
		print("damn its cold!")
main()