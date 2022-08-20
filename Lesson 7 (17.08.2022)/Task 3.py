class Cell:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return Cell(self.number + other.number)

    def __sub__(self, other):
        if self.number < other.number: raise Exception("Нельзя из большего вычесть меньшее")
        return Cell(self.number - other.number)

    def __mul__(self, other):
        return Cell(self.number * other.number)

    def __truediv__(self, other):
        return Cell(self.number // other.number)

    def __str__(self):
        return f"Number of cells in cell {self.number}"

    def make_order(self, cell_in_line):
        text = '\n'.join(["*" * cell_in_line for i in range(self.number // cell_in_line)])
        if self.number % cell_in_line != 0:
            text += '\n' + "*" * (self.number % cell_in_line)
        return text


cell_1 = Cell(26)
cell_2 = Cell(10)

cell_3 = cell_1 + cell_2 + cell_1
print(cell_3)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_3.make_order(10))
