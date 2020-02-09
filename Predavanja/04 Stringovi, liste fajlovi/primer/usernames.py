def main():
	first_name = input("first name: ")
	last_name = input("last name: ")
	username = first_name[0]+last_name[:7]
	print("username: "+username)
main()