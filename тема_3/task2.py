def func(name, surname, year, city, email, phone):
    print(f'Пользователь {name} {surname} {year} года рождения. Проживает в городе {city}. Эмейл - {email}, '
          f'телефон - {phone}')
    return name, surname, year, city, email, phone


func(name = str(input("Введите Ваше имя: ")), surname = str(input("Введите Вашу фамилию:")),
     year = int(input("Введите Ваш год рождения:")), city = str(input("Где Вы проживаете? ")),
     email = input("Введите Ваш электронный адрес:"), phone=input("Введите Ваш телефон: "))

