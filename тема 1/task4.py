n = int(input("Введите целое положительное число"))
last = n % 10
while n <=0:
    n = int(input("ОШИБКИ!Введите целое положительное число"))
while n > 0:
    if n % 10 > last:
        last = n % 10
    n = n // 10
print("Наибольшая цифра", last)










