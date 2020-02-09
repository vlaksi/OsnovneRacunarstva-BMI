namesF = open("names.txt", "r")
namesFOut = open("namesOut.txt","w")
#names = namesF.readlines()
for name in namesF:
	print(name.strip().split()[0][0]+name.strip().split()[1][:7], file=namesFOut)
namesF.close()
namesFOut.close()