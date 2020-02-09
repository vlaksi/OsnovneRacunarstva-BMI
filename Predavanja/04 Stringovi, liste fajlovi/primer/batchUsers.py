def main():
	users_file = open("users.txt","r")
	usernames_file = open("usernames.txt","w")
	users_lines = users_file.readlines()
	for line in users_lines:
		user = line.split()
		print(user[0][0].lower()+user[1][:7].lower(),file = usernames_file)
	users_file.close()
	usernames_file.close()

main()