class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        x = ''
        for i in range(len(self.data)):
            x = x + ' '.join(map(str, self.data[i])) + '\n'
        return x

    def __add__(self, other):
        if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]):
            print('Матрицы отличаются размерами!')
        result = []
        for i in range(0, len(self.data)):
            result.append([])
            for j in range(0, len(self.data[i])):
                result[i].append(self.data[i][j] + other.data[i][j])
        return Matrix(result)


m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

print(f'Первая матрица \n'
      f'{m1} \n'
      f'Вторая матрица \n'
      f'{m2} \n'
      f'Результат сложения матриц \n'
      f'{m1 + m2}')
