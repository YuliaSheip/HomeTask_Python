# season_list = ["Зима", "Весна", "Лето", "Осень"]
# n = int(input("Введите номер месяца: "))
# if 1 <= n <= 2 or n == 12:
#     print(season_list[0])
# elif 3 <= n <= 5:
#     print(season_list[1])
# elif 6 <= n <= 8:
#     print(season_list[2])
# elif 9 <= n <= 11:
#     print(season_list[3])
# else:
#     print("Ошибка!")

season_dict = {1: "Зима", 2: "Зима", 3: "Весна", 4: "Весна", 5: "Весна", 6: "Лето",7: "Лето", 8: "Лето",
               9: "Осень", 10: "Осень", 11: "Осень", 12: "Зима"}
key = int(input("Введите номер месяца: "))
if 1 <= key <= 12:
    print(season_dict.get(key))
else:
    print("Ошибка!")