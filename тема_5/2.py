number = 0
f_obj = open("file_2.txt", 'r')
content = f_obj.read()
content_list = content.split("\n")
print(f"В тексте {len(content_list)} строк")
while number < len(content_list):
    for el in content_list:
        word = el.split(" ")
        number += 1
        print(f" В строке {number} {len(word)} слов")
f_obj.close()



