from functools import reduce

new_list = [el for el in range(100, 1001) if el % 2 == 0]
print(new_list)

def my_func (previous_el, el):
    return previous_el * el

print(reduce(my_func, new_list))
