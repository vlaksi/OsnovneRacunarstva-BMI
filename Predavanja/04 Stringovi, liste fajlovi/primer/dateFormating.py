def main():
	date_unformated = input("date: ")
	months = ["January", "February", "March", "April", "May"]
	date_formated = ""
	date_tokens = date_unformated.split(".")
	date_formated += str(int(date_tokens[0]))+". "+months[int(date_tokens[1])-1]+" "+date_tokens[2]+"."
	print(date_formated)

main()