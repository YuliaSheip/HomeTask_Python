my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result_list = [el for index, el in enumerate(my_list) if my_list[index] > my_list[index-1] and index != 0]
print(result_list)
