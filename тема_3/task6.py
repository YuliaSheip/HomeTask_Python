word = input("Введите слово с маленькой буквы: ")
def int_func():
    capital_word = word.capitalize()
    return capital_word
print(int_func())

source = input("Please enter string in small letters: ").split()
final_string = []
for el in source:
    word = el
    final_string.append(int_func())
print(' '.join(final_string))



