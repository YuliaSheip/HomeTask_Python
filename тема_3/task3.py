# def func():
#     list = input("Введите 3 числа через пробел: ").split()
#     max_number = int(max(list))
#     index_max = list.index(max(list))
#     list.pop(index_max)
#     second_max_number = int(max(list))
#     result = max_number + second_max_number
#     return result
# print(func())


a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

def func(a, b, c):
    if a >= b >= c:
        result = a + b
        return result
    elif b >= c >= a:
        result = b + c
        return result
    elif a >= c >= b:
        result = a + c
        return result

print(func(a, b, c))
