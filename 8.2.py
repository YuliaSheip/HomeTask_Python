class MyOwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

inp_data1 = int(input("Введите делимое: "))
inp_data2 = int(input("Введите делитель: "))

try:
    if inp_data2 == 0:
        raise MyOwnError("Будьте внимательны. Деление на ноль недопустимо")
    else:
        result = inp_data1 / inp_data2
except ValueError:
    print("Вы ввели не число")
except MyOwnError as err:
    print(err)
else:
    print(f"Все хорошо. Рузультат: {result}")


