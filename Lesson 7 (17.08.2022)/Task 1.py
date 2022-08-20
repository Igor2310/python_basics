class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        text = ""
        for x in self.matrix:
            for y in x:
                text += str(y) + ' '
            text = text.strip()
            text += '\n'
        return text.strip()

    def __add__(self, other):
        if [len(i) for i in other.matrix] != [len(i) for i in self.matrix]:
            raise Exception("Нельзя сложить данные матрицы, так как размерность матриц должно быть одинакого")
        lst = [list(map(lambda x, y: x + y, i[0], i[1])) for i in zip(self.matrix, other.matrix)]
        return Matrix(lst)


mx1 = Matrix([[31, 32], [2, 2]])
mx2 = Matrix([[31, -32], [0, -6]])
mx3 = Matrix([[31, 32], [6, 2]])

print(mx1)
print("-" * 20)
print(mx1 + mx2 + mx3 )
print("-" * 20)
