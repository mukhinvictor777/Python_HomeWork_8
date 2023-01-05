"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы.
[[], [], []]...
"""


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        for row in self.matrix:
            for i in row:
                print(f'{i:4}', end='')
            print()

    def __add__(self, other):
        for i in range(len(self.matrix)):
            for j in range(len(other.matrix[i])):
                self.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return Matrix.__str__(self)


my_matrix = Matrix([[-5, 2, 4, 6], [1, 10, -1, 4], [8, 4, -5, 2], [7, -6, 10, -5]])
next_matrix = Matrix([[-2, 8, 4, -5], [10, 5, 4, 7], [-8, 6, 6, 10], [3, -6, 10, -2]])
my_matrix.__str__()
print()
next_matrix.__str__()
print()
new_matrix = my_matrix + next_matrix


