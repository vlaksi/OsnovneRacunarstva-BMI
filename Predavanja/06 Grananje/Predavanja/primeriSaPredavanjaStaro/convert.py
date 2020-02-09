def main():
	c = eval(input("What is the Celsius temperature? "))
	f = 9/5 * c + 32
	if f<30:
		x = 3
		print("It's very cold!")
		print("bla bla bla")
	print(x)
	if f >90:
		print("It's very hot !")
	if int(f)%2!=0:
		print("It's odd !")
	print("The temperature is", f, "degrees Fahrenheit.")
main()