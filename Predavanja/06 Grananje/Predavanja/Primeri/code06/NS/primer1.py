def main():
	c = eval(input("What is the Celsius temperature? "))
	f = 9/5 * c + 32
	print("The temperature is", f, "degrees Fahrenheit.")
	if f>90:
		print("Very hot!")
	elif f<0:
		print("Very cold!")
	else:
		print("Just right")
main()