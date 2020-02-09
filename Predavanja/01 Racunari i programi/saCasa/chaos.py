# File: chaos.py
# A simple program illustrating chaotic behavior.

print("This program illustrates a chaotic function")
# take a value from the input and convert it to number
x = eval(input("Enter a number between 0 and 1: "))
for i in range(10):
    x = 3.9 * x * (1 - x)
    print(x)