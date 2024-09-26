import json
from datetime import datetime

students = json.load(open("students.json", "r", encoding="utf-8"))

# dateN = input("Дата N (%d.%m.%y): ")
dateN = "10.10.2025"

for znum in students:
	fio = students[znum]["lname"]+" "+students[znum]["name"]+" "+znum
	fioprinted = 0
	for ekz in students[znum]["ekz"]:
		if datetime.strptime(dateN, "%d.%m.%Y") < datetime.strptime(students[znum]["ekz"][ekz]["date"], "%d.%m.%Y"):
			if not fioprinted: print("|", f"{fio:-^70}", "|", "-"*19, "|", "-"*9, "|"); fioprinted = 1
			print(f"|{ekz:^72}|{students[znum]['ekz'][ekz]['prepod']:^21}|{students[znum]['ekz'][ekz]['date']:^11}|")