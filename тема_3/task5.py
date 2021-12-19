def func():
    int_list = []
    symbol = "~"
    n = 1
    while n >= 1:
        source = input("Введите числа через пробел или символ ~ для завершения сессии").split()
        if source[0] == symbol:
            print("Сессия завершена")
            break
        elif len(source) >= 2 and source[-1] == symbol:
            source.remove(source[-1])
            for el in source:
                el = int(el)
                int_list.append(el)
            result = sum(int_list)
            print("Сессия завершена")
            return result
            break
        else:
            n = n + 1
            for el in source:
                el = int(el)
                int_list.append(el)
            result = sum(int_list)
            print(result)
    return result
print(func())


