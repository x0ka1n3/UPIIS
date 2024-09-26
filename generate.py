import json
import random


subs = ["Сети и системы передачи информации", "Методы и средства криптографической защиты информации", "Безопасность вычислительных сетей", "Программно-аппаратные средства защиты информации", "Биометрические системы аутентификации", "Средства контроля эффективности мер защиты информации", "Управление доступом к ресурсам автоматизированных систем", "Безопасность операционных систем", "Безопасность систем баз данных", "Угрозы информационной безопасности автоматизированных систем", "Администрирование систем защиты информации автоматизированных систем", "Защита информации от утечки по техническим каналам", "Стандарты информационной безопасности", "Основы системы лицензирования и сертификации в области защиты информации", "Разработка политики информационной безопасности", "Управление рисками информационной безопасности автоматизированных систем", "Разработка систем защиты информации автоматизированных систем", "Организационное и правовое обеспечение информационной безопасности", "Основы управления информационной безопасностью", "Организация защиты персональных данных в информационных системах"]

students = {}

lastnames	= ["Иванов", "Петров", "Сидоров", "Лебедев", "Жуков", "Карпов", "Смирнов"]
firstnames	= ["Александр/Александра", "Евгений/Евгения", "Валентин/Валентина", "Виктор/Виктория", "Ян/Яна"]

for i in range(100):
	lnr = random.randint(0, len(lastnames)-1)
	fnr = random.randint(0, len(firstnames)-1)
	g = random.randint(0,1)

	lname = lastnames[lnr]+"а" if g==1 else lastnames[lnr]
	fname = firstnames[fnr].split("/")[g]


	day = random.randint(1,28)
	month = random.randint(1,12)
	year = random.randint(1999, 2003)

	znum = str((year+18)%100)+"Б"+f"{i:04}"



	k = random.randint(3,5)
	ekzes = random.choices(subs, k=5)

	ekzlist = {}

	ekzmonth = random.randint(0,1)
	ekzyear = random.randint(2024, 2025)
	for sub in ekzes:
		plnr = random.randint(0, len(lastnames)-1)
		pfnr = random.randint(0, len(firstnames)-1)
		pg = random.randint(0,1)

		plname = lastnames[plnr]+"а" if pg==1 else lastnames[plnr]
		pfname = firstnames[pfnr].split("/")[pg]

		ekzday = random.randint(1,28)

		ekzlist.update({sub:{"date":f"{ekzday}.{'1' if ekzmonth == 0 else '6'}.{ekzyear}", "prepod":f"{plname} {pfname}"}})

	students.update({znum:
		{
		"name": fname,
		"lname": lname,
		"dob": f"{day}.{month}.{year}",
		"ekz": ekzlist
		}
		})

json.dump(students, open("students.json", "w", encoding="utf-8"), ensure_ascii=False, indent=4)