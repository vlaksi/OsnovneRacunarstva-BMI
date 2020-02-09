import codecs

def load_students():
	# ucitati fajl sa studentima
	f = codecs.open("studenti.txt","r",encoding="utf8")
	lines = f.readlines()
	f.close()
	students = []
	for line in lines:
		student = str_2_student(line)
		# recnik dodati u listu studenata
		students.append(student)
	return students
	# vratiti listu studenata

def str_2_student(s):
	# E3|Duško|Korac|Mitar|12.12.1953.|1212953800028|Fruskogorska 20|064/123321|dusko@gmail.com|3
	l = s.split("|")
	# svaki red iz fajla konvertovati u recnik
	student = {"indeks":l[0],
		"ime":l[1],
		"prezime":l[2],
		"ime_roditelja":l[3],
		"datum_rodjenja":l[4],
		"jmbg":l[5],
		"adresa":l[6],
		"broj_telefona":l[7],
		"email":l[8],
		"godina":l[9]}
	return student

def save_students(students):
	f = codecs.open("studenti1.txt","w",encoding="utf8")
	# prodji kroz listu studenata
	for student in students:
		# svakog studenta konvertuj u string
		s_student = student_2_str(student)
		# snimi svaki string u fajl
		f.write(s_student)
	# zatvori fajl
	f.close()

def student_2_str(student):
	str_student = "|".join([student["indeks"],
			student["ime"],
			student["prezime"],
			student["ime_roditelja"],
			student["datum_rodjenja"],
			student["jmbg"],
			student["adresa"],
			student["broj_telefona"],
			student["email"],
			student["godina"],
			])
	return str_student	

def find_student(indeks, students):
	for student in students:
		if student["indeks"]==indeks:
			return student
	return None

def search_students(last_name, students):
	ret_val = []
	for student in students:
		if student["prezime"]==last_name:
			ret_val.append(student)
	return ret_val

# broj indeksa|ime         |prezime         |ime roditelja   | ... 
#-------------+------------+----------------+----------------+ ...
# E2          |Pera        |Preic           |Stevan          | ...
# E2          |Pera        |Preic           |Stevan          | ...
# E2          |Pera        |Preic           |Stevan          | ...
# E2          |Pera        |Preic           |Stevan          | ...
# E2          |Pera        |Preic           |Stevan          | ...

def format_header():
	ret_val = "indeks|ime       |prezime     |ime roditelja|\n------+----------+------------+-------------+"
	return ret_val

def format_student(student):
	# ret_val = student["indeks"]+"|"+student["ime"]+"|"+student["prezime"]+"|"+student["ime_roditelja"]
	ret_val = "{0:6}|{1:10}|{2:12}|{3:13}".format(
		student["indeks"][:6],
		student["ime"][:10],
		student["prezime"][:12],
		student["ime_roditelja"][:13]);
	return ret_val

def format_all_students(students):
	ret_val = ""
	for student in students:
		ret_val+=format_student(student)+"\n"
	return ret_val

# def get_ime(student):
# 	return student["ime"]

def sort_by_name(students):
	students.sort(key=lambda x : x["ime"])

def update_student(students, indeks, address, phone, email):
	student = find_student(indeks,students)
	student["adresa"] = address
	student["broj_telefona"] = phone
	student["email"] = email
	save_students(students)

def add_student(students, indeks, ime, prezime, ime_roditelja, datum_rodjenja, jmbg, adresa, broj_telefona, email):
	student = {"indeks":indeks,
		"ime":ime,
		"prezime":prezime,
		"ime_roditelja":ime_roditelja,
		"datum_rodjenja":datum_rodjenja,
		"jmbg":jmbg,
		"adresa":adresa,
		"broj_telefona":broj_telefona,
		"email":email,
		"godina":"1"}
	if already_exists(students, student):
		print("vec postoji student sa tim brojem indeksa ili jmbg!")
		return
	students.append(student)
	save_students(students)

def already_exists(students, student):
	for s in students:
		if s["jmbg"]==student["jmbg"] or s["indeks"]==student["indeks"]:
			return True
	return False

def main():
	# students = search_students("Kovinjalo")
	students = load_students()
	# header = format_header()
	# sort_by_name(students)
	# s_students = format_all_students(students)
	# print(s_students)
	# update_student(students,"E2","Proba A","Proba T", "Proba E")
	add_student(students, "E12", "Proba", "Proba", "Proba", "Proba", "Proba", "Proba", "Proba", "Proba")

if __name__ == '__main__':
	main()