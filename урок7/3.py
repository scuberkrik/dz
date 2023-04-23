class Cell:
    def __init__(self, cells_num):
        self.cells_num = int(cells_num)

    def __add__(self, other):
        return Cell(self.cells_num + other.cells_num)

    def __sub__(self, other):
        if self.cells_num - other.cells_num > 0:
            return Cell(self.cells_num - other.cells_num)
        else:
            print("Вычитание невозможно")

    def __mul__(self, other):
        return Cell(self.cells_num * other.cells_num)

    def __truediv__(self, other):
        return Cell(self.cells_num // other.cells_num)

    def make_order(self, cells_per_row):
        row = '*' * cells_per_row
        return '\n'.join([row for _ in range(self.cells_num // cells_per_row)]
                         ) + '\n' + '*' * (self.cells_num % cells_per_row)


cell1 = Cell(9)
cell2 = Cell(13)

print(cell1.make_order(3))
print(cell2.make_order(5))

cell3 = cell1 + cell2
print(cell3.cells_num)

cell4 = cell2 - cell1
print(cell4.cells_num)

cell5 = cell2 * cell1
print(cell5.cells_num)

cell6 = cell2 / cell1
print(cell6.cells_num)
