from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, param):
        self.param = param

@abstractmethod
def fabrics(self):
    pass

class Coat(Clothes):
    def __init__(self, param):
        super().__init__(param)

    @property
    def fabrics(self):
        fabrics_to_by = self.param/6.5 + 0.5
        return fabrics_to_by

class Suit(Clothes):
    def __init__(self, param):
        super().__init__(param)
    @property
    def fabrics(self):
        fabrics_to_buy = 2*self.param + 0.3
        return fabrics_to_buy

my_coat = Coat(2)
print(f"For the coat you need to buy {my_coat.fabrics} m of fabrics")
my_suit = Suit(6)
print(f"For the suit you need to buy {my_suit.fabrics} m of fabrics")
