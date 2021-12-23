class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationery):
    def draw(self):
        print("Запуск отрисовки ручкой")

class Pencil:
    def draw(self):
        print("Запуск отрисовки иягким карандашом")

class Handle:
    def draw(self):
        print("Запуск отрисовки маркером")

tool_1 = Pen("pen")
tool_1.draw()
tool_2 = Pencil("pencil")
tool_2.draw()
tool_3 = Handle("handle")
tool_3.draw()