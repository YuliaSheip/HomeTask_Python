class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt(self):
        self.weight_km = input("Введите массу асфальта на км в кг: ")
        self.road_sm = input("Введите толщину полотна в см: ")
        self.total_weight = (self._length * self._width * int(self.weight_km) * int(self.road_sm))/1000
        print(f"Масса асфальта {self.total_weight} тонн")

road_1 = Road(5000, 20)
road_1.asphalt()






