a = float(input("Введите делимое: "))
b = float(input("Введите делитель: "))
def my_division(a, b):
    try:
        result = float(a / b)
        return result
    except ZeroDivisionError:
        print("На ноль делить нельзя")

print(my_division(a, b))





