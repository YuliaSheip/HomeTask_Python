class Car:
    def __init__(self, speed, color,name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась")

    def turn(self, direction):
        print(f"Машина повернула {direction}")

    def show_speed(self):
        print(f"Скорость машины {self.speed}")

class TownCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("Превышение скорости!")
        else:
            print(f"Скорость машины {self.speed}")

class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police = False)

class WorkCar(Car):
    def show_speed(self):
        if speed > 60:
            print("Превышение скорости!")
        else:
            print(f"Скорость машины {self.speed}")

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police = True)

car_1 = PoliceCar(200,"black", "volvo", True)
car_1.go()
car_1.show_speed()
car_1.turn("left")
car_1.stop()
car_2 = TownCar(50, "red", "ford", False)
car_2.go()
car_2.show_speed()
car_2.turn("right")
car_2.stop()
car_3 = WorkCar(50, "yellow", "audi", False)
car_3.go()
car_3.show_speed()
car_3.turn("left")
car_3.stop()
car_4 = SportCar(350, "blue", "ferrari", False)
car_4.go()
car_4.show_speed()
car_4.stop()






