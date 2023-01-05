"""
Реализовать программу работы с органическими клетками, состоящими из ячеек.
Необходимо создать класс Клетка (Cell).
В его конструкторе инициализировать параметр (quantity),
соответствующий количеству ячеек клетки (целое число).
"""


class Cell:
    def __init__(self, quantity):
        try:
            int(quantity)
        except ValueError:
            print(f'Количество ячеек может быть только целым числом')
        quantity = int(quantity)
        if quantity < 1:
            print(f'Количество ячеек может быть только целым числом больше нуля')
        else:
            self.quantity = quantity

    def __add__(self, other):
        return f'Число ячеек общей клетки равно, полученной в результате сложения двух клеток равно: ' \
               f'{self.quantity + other.quantity}'

    def __sub__(self, other):
        if self.quantity > other.quantity:
            return f'Число ячеек общей клетки равно, полученной в результате вычитания двух клеток равно: ' \
                   f'{self.quantity - other.quantity}'
        else:
            return f'Нельзя произвести вычитание данных клеток. Первая клетка должна быть строго больше второй '

    def __mul__(self, other):
        return f'Число ячеек общей клетки, полученной в результате умножения двух клеток равно: ' \
               f'{self.quantity * other.quantity}'

    def __truediv__(self, other):
        return f'Число ячеек общей клетки, полученной в результате деления двух клеток равно: ' \
               f'{self.quantity // other.quantity}'

    def make_order(self, row):
        result = ''
        for i in range(self.quantity // row):
            result += '*' * row + '\n'
        result += '*' * (self.quantity % row)
        return result


cell1 = Cell(30)
cell2 = Cell(25)
cell3 = Cell(10)
cell4 = Cell(15)

print()
print("Складываем")
print(cell1 + cell2)
print()
print("Вычитаем")
print(cell2 - cell1)
print(cell4 - cell3)
print()
print("Умножаем")
print(cell2 * cell1)
print()
print("Делим")
print(cell1 / cell2)
print()

print("Организация ячеек по рядам")
print()
print(cell1.make_order(5))
print(cell2.make_order(10))
