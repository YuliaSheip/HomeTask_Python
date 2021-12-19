f_obj = open("my_file_1.txt", 'x')

while True:
    my_string = input("Введите cтроку:")
    if not my_string:
        break
    else:
        my_string += "\n"
        f_obj.write(my_string)
f_obj.close()
j