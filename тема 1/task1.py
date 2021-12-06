name: str = "Юля"
age = 31
occupation = "бизнес-аналитик"
length = 1

print("Добрый день,","я", name)
print("Мне", age, "год")
print("Работаю как", occupation, length, "год")

friend_name = input("А как тебя зовут?")
print(friend_name, ", рада знакомству")
work_status = input("Ты работаешь?")
if work_status == "да":
    print(input("Здорово, а кем?"))

