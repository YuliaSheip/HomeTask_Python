f_obj = open("file_4.txt", 'r')
f_obj2 = open("file_4.1.txt", "w")

translation = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
content = f_obj.readlines()
new_content = []
for el in content:
    eng, number = el.rstrip().split(" - ")
    eng = translation.get(eng)
    new_content = eng + " - " + number + "\n"
    f_obj2.write(new_content)
f_obj2.close()
f_obj.close()