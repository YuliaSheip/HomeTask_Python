my_string = input("Введите слова через пробел: ").split()
for ind, el in enumerate(my_string, 1):
    if len(el) > 10:
        print(ind, el[0:10])
    else:
        print(ind, el)


