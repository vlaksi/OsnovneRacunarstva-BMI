s = input("unesi vrednost: ")
num = ""
for ch in s:
	num += str(ord(ch)) + " "
num = num[:-1]
print(num)