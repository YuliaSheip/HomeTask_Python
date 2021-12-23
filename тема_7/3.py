class Cell:
    def __init__(self, number):
        self.number = int(number)
        if self.number <= 0:
            print("Cell doesn't exist")

    def __add__(self, other):
        return Cell(self.number + other.number)

    def __sub__(self, other):
        if self.number < other.number:
            print("Невозможно вывести значение")
            return
        else:
            return Cell(self.number - other.number)

    def __mul__(self, other):
        return Cell(self.number * other.number)

    def __truediv__(self, other):
        return Cell(self.number // other.number)

    def make_order (self, quantity):
        try:
            return ("*" * quantity + "\n") * (self.number // quantity) + "*" * (self.number % quantity)
        except:
            print("Error")

cell_1 = Cell(12)
cell_2 = Cell(0)
cell_3 = cell_1 * cell_2
print(cell_1.make_order(5))
