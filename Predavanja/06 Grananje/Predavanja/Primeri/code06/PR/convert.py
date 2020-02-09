def main():
	c = eval(input("What is the Celsius temperature? "))
	f = 9/5 * c + 32
	print("The temperature is", f, "degrees Fahrenheit.")
	if f>=90:
		print("very hot!")
	if f<=30:
		print("very cold!")
main()