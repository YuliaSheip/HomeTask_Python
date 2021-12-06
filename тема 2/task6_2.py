item_number = 0
my_dict = {"Название": "", "Цена": "", "Количество": "", "Единица измерения": ""}
goods_list = []
name_list = []
price_list = []
qty_list = []
u_m_list = []
analytics = {"Название": name_list, "Цена": price_list, "Количество": qty_list, "Единица измерения": u_m_list}
while input("Хотите добавить товар? Да/Нет: ") == 'Да':
    name = input("Введите название товара: ")
    price = float(input("Укажите цену товара: "))
    qty = int(input("Укажите количество товара: "))
    u_m = str(input("Укажие единицу измерения товара: "))
    item_number = item_number + 1
    new_dict = {"Название": name, "Цена": price, "Количество": qty, "Единица измерения": u_m}
    my_dict.update(new_dict)
    my_tuple = (item_number, my_dict)
    goods_list.append(my_tuple)
    print(goods_list)
    name_list.append(my_dict.get("Название"))
    price_list.append(my_dict.get("Цена"))
    qty_list.append(my_dict.get("Количество"))
    u_m_list.append(my_dict.get("Единица измерения"))
    print(analytics)



