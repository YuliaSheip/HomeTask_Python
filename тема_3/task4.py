x = int(input("Введите X: "))
y = int(input("Введите Y: "))

def func (x, y):
    if x > 0 and y < 0:
        result = x ** y
        return result
    else:
        print("Введенные данные не соответстуют условию задачи")
print(func(x, y))