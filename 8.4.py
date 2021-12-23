class Warehouse:

    equipment_report = {}

class OfficeEquipment:

    def __init__(self, title, uid, price, producer, in_warehouse = False):
        self.title = title
        self.uid = uid
        self.price = price
        self.producer = producer
        self.in_warehouse = in_warehouse
        try:
            isinstance(price, float)
            if False:
                raise ValueError
            else:
                self.price = price
        except ValueError:
            print("Неверный формат входных данных!")


    def add_to_storage (self):
        if self.in_warehouse == False:
            equipment_per_item_info = [self.uid, self.price, self.producer]
            equipment_per_type_info = Warehouse.equipment_report.get(self.title, [])
            self.in_warehouse = True
            if self.title in Warehouse.equipment_report.keys():
                equipment_per_type_info.append(equipment_per_item_info)
            else:
                equipment_per_type_info.append(equipment_per_item_info)
                Warehouse.equipment_report[self.title] = equipment_per_type_info
            print(f"New {self.title} has been placed to warehouse")
            print(Warehouse.equipment_report)
        else:
            print("The item is already in the warehouse")

    def remove_from_storage(self):
        if self.in_warehouse == True:
            equipment_per_item_info = [self.uid, self.price, self.producer]
            equipment_per_type_info = Warehouse.equipment_report.get(self.title, [])
            self.in_warehouse = False
            equipment_per_type_info.remove(equipment_per_item_info)
            print(f" {self.title} has been deleted from the  warehouse")
            print(Warehouse.equipment_report)
        else:
            print("The item is not in the warehouse")



class Scanner(OfficeEquipment):

    def __init__(self, title, uid, price, producer, in_warehouse, resolution):
        self.title = title
        self.uid = uid
        self.price = price
        self.producer = producer
        self.in_warehouse = in_warehouse
        self.resolution = resolution

class Printer(OfficeEquipment):
    def __init__(self, title, uid, price, producer, in_warehouse, is_color):
        self.title = title
        self.uid = uid
        self.price = price
        self.producer = producer
        self.in_warehouse = in_warehouse
        self.is_color = is_color

class Xerox(OfficeEquipment):
    def __init__(self, title, uid, price, producer, in_warehouse, origin):
        self.title = title
        self.uid = uid
        self.price = price
        self.producer = producer
        self.in_warehouse = in_warehouse
        self.origin = origin

printer1 = Printer("Printer", 1, 25, "Samsung", False, True)
scan1 = Scanner("Scanner", 36, 10, "Xiomi", False, 305)
printer1.add_to_storage()
scan1.remove_from_storage()

