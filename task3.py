"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class ZeroDivError(Exception):
    def __init__(self, txt):
        self.txt = txt


def div():
    divisible = input('Введите целое число: ')
    divider = input('Введите целое число, отличное от нуля: ')
    try:
        divisible = int(divisible)
        divider = int(divider)
        if divider == 0:
            raise ZeroDivError('Делить на ноль нельзя!')
        else:
            return divisible / divider
    except ValueError:
        return f'Вы ввели не число'
    except ZeroDivError as err:
        return err


print(div())
