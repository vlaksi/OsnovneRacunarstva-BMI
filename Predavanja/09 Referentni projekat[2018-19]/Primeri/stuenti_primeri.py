import codecs

def loadStudents():
    checkFile()
    for line in codecs.open('studenti.txt', 'r',encoding='utf8').readlines():
        if len(line) > 1:
            stud = str2student(line)
            studenti.append(stud)

def checkFile():
    if not exists('studenti.txt'):
        codecs.open('studenti.txt', 'w',encoding='utf8').close()

def saveStudents():
    file = codecs.open('studenti.txt', 'w',encoding='utf8')
    for stud in studenti:
        file.write(student2str(stud))
        file.write('\n')
    file.close()

def str2student(line):
    if line[-1] == '\n':
        line = line[:-1]
	# line = line.strip() 
    indeks, ime, prezime, roditelj, datum, jmbg, adresa, telefon, email, godina = line.split('|')
    stud = {
      'indeks': indeks,
      'ime': ime,
      'prezime': prezime,
      'roditelj': roditelj,
      'datum': datum,
      'jmbg': jmbg,
      'adresa': adresa,
      'telefon': telefon,
      'email': email,
      'godina': godina
    }
    return stud

def student2str(stud):
    return '|'.join([stud['indeks'], stud['ime'], stud['prezime'], 
      stud['roditelj'], stud['datum'], stud['jmbg'], stud['adresa'], 
      stud['telefon'], stud['email'], stud['godina']])
