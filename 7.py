from functools import reduce
n = int(input("Введите число: "))
def fact(n):
    my_list = [el for el in range (1, n+1)]
    def my_func(previous_el, el):
        return previous_el * el
    yield reduce(my_func, my_list)
print(fact(n))

for el in fact(n):
    print(el)



