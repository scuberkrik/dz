class Road:
    _weight = 0.025  # вес 1кв.м. полотна толщиной 1см

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_weight(self, thickness):
        ret_val = self._length * self._width * thickness * self._weight
        return ret_val


x = Road(5000, 20)
y = x.get_weight(5)

print(f'Вес асфальта, требуемый для укладки дороги, равен {y} т.')
