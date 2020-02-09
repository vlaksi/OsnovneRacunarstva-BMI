def encoder():
	text = input("s: ")
	encoded = ""
	for character in text:
		encoded += str(ord(character))+" "
	print(encoded)

def decoder():
	text = input("code: ")
	decoded = ""
	for coded_character in text.split():
		decoded += chr(int(coded_character))
	print(decoded)

decoder()