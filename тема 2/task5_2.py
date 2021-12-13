my_list = [7, 5, 3, 3, 2]
i = 0
while len(my_list) <= 100:
    rating = int(input("Введите рейтинг: "))
    for el in my_list:
        if rating < 0:
            print("Error")
        if el == rating:
            my_list.insert(my_list.index(el) + 1, rating)
            break
        if el < rating:
            my_list.insert(0, rating)
            break
        if my_list[-1] > rating:
            my_list.append(rating)
            break
        if my_list[i] > rating > my_list[i + 1]:
            my_list.insert(my_list.index(el) + 1, rating)
            break
    print(my_list)



