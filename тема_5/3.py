f_obj = open("file_3.txt", 'r')
content = f_obj.read()
content_list = content.split("\n")[1:]
low_salary = []
salaries_list = []
for el in content_list:
    surname, salary = el.split(", ")
    salary = int(salary)
    salaries_list.append(salary)
    if salary < 20:
        low_salary.append(surname)
print(f"Зарплата ниже 20 тыс рублей у {low_salary}")
av_salary = sum(salaries_list)/len(salaries_list)
print(f"Средняя зарплата {av_salary} тыс рублей")
f_obj.close()




