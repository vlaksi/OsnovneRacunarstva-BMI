def main():
    c = eval(input("What is the Celsius temperature? "))
    f = 9/5 * c + 32
    print("The temperature is", f, "degrees Fahrenheit.")
    if f >= 90:
        print("It's really hot out there, be careful!")
    if f <= 30:
        print("Brrrrr. Be sure to dress warmly")

main()
