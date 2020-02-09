def main():
	file_name = input("file name: ")
	file_to_read = open(file_name,"r")
	data = file_to_read.read()
	print(data)
	file_to_read.close()
main()