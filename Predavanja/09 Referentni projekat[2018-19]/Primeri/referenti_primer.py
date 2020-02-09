import codecs

def load_refs():
	# otvoriti fajl
	f = codecs.open('referenti.txt', 'r',encoding='utf8')
	# citati red po red
	redovi = f.readlines()
	f.close()
	# svaki red konvertovati u recnik
	referenti = []
	for red in redovi:
		# svaki recnik dodati u listu
		# print(red)
		referent=str_to_ref(red)
		referenti.append(referent)
	return referenti

def str_to_ref(str_ref):
	l_ref = str_ref.strip().split("|")
	referent = {"ime":l_ref[0],
		"prezime":l_ref[1],
		"username":l_ref[2],
		"password":l_ref[3]}
	return referent

def ref_to_str(ref):
	# return ref["ime"]+"|"+ref["prezime"]+"|"+ref["username"]+"|"+ref["password"]
	return "|".join(ref["ime"],ref["prezime"],ref["username"],ref["password"])

def login(username, password):
    for ref in referenti:
        if ref['username'] == username and ref['password'] == password:
            return True
    return False

referenti = load_refs()

def main():
	username = input("username: ")
	password = input("password: ")
	while not login(username, password):
		print("uneli ste pogresno korisnicko ime ili lozinku")
		username = input("username: ")
		password = input("password: ")
	print("uspesno ste se prijavili na sistem")
	# referenti = load_refs()
	# for ref in referenti:
	# 	print(ref_to_str(ref))

if __name__ == '__main__':
	main()