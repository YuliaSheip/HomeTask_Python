from itertools import count
from itertools import cycle


# final = int(input("Введите финальное значение: "))
# for el in count(int(input("Введите стартовое значение: ")), 1):
#     if el > final:
#         break
#     else:
#         print(el)

my_list = ["random text", True, 3, None, 105]
n = 1
for el in cycle(my_list):
    n += 1
    if n > 8:
        break
    else:
        print(el)

