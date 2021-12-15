f_obj = open("my_file_5.txt", 'w+', encoding = "utf-8")

numbers = input("Введите числа через пробел: ")
print(numbers, file=f_obj)

content = f_obj.read().rstrip().split()
print(content)
numbers_list = [int(el) for el in content if el.isdigit()]
print(numbers_list)
print(sum(numbers_list))

f_obj.close()