my_list = list(input("Введите элементы списка: "))
n = len(my_list) % 2
if n == 0:
    my_list[::2], my_list[1::2] = my_list [1: :2], my_list[::2]
    print(my_list)
else:
    last_el = my_list.pop(-1)
    my_list[::2], my_list[1::2] = my_list[1::2], my_list[::2]
    my_list.append(last_el)
    print(my_list)



