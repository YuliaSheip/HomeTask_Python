class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def get_full_name(self):
        full_name = self.name + " " + self.surname
        return full_name

    def get_total_income(self):
        total_income = self._income["wage"] + self._income["bonus"]
        return total_income

analyst = Position("Yulia", "Sheipak", "analyst", 100, 25)
analyst.get_full_name()
analyst.get_total_income()
print(f"The total income of {analyst.get_full_name()} will be {analyst.get_total_income()}" )

