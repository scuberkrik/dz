from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def fabric_consumption(self):
        pass


class Coat(Clothes):

    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    @property
    def fabric_consumption(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):

    def __init__(self, name, height):
        super().__init__(name)
        self.height = height

    @property
    def fabric_consumption(self):
        return 2 * self.height + 0.3


def total_fabric_consumption(my_list):
    total = 0
    for i in my_list:
        total += i.fabric_consumption
    return total


coat = Coat("Пальто", 45)
suit = Suit("Костюм", 110)

print("Расход ткани для пальто:", coat.fabric_consumption)
print("Расход ткани для костюма:", suit.fabric_consumption)

clothes_list = [coat, suit]
print("Суммарный расход ткани:", total_fabric_consumption(clothes_list))
