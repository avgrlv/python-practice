import math
from math import log10


class Operation:

    def __init__(self, op, title, foo):
        super().__init__()
        self.op = op
        self.title = title
        self.foo = foo

    def __call__(self, *args):
        return self.foo(*args)


Operation.nop = Operation("", "Идентичность", lambda x, y: x)


class CalculatorTask:
    def __init__(self):
        super().__init__()

        self.operations = {
            o.op: o for o in [
                Operation('*', 'Умножение', lambda a, b: a * b),
                Operation('+', 'Сложение', lambda a, b: a + b),
                Operation('-', 'Вычитание', lambda a, b: a - b),
                Operation('/', 'Деление', lambda a, b: a / b),
                Operation('//', 'Целочисленное деление двух чисел', lambda a, b: a // b),
                Operation('**', 'Возведение в степень', lambda a, b: a ** b),
                Operation('%', 'Получение остатка от деления', lambda a, b: a % b),
                Operation('log10', 'Логорифм первого числа по основанию 10', lambda a, b: log10(a)),
                Operation('>', 'Строго больше', lambda a, b: a > b),
                Operation('=>', 'Больше или равно', lambda a, b: a >= b),
                Operation('<', 'Строго меньше', lambda a, b: a < b),
                Operation('<=', 'Меньше или равно', lambda a, b: a <= b),
                Operation('=', 'Равны', lambda a, b: a == b),
                Operation('!=', 'Не равны', lambda a, b: a != b),
            ]}

    def print_operations(self):
        message = 'Доступные математические операции:\n'
        for operation in self.operations.values():
            message += (operation.op + '\t:\t' + operation.title + "\n")
        message += "Введите операцию: "
        return message

    def calculate(self, first_number, second_number, operation):
        print(f"Результат: {self.operations.get(operation, Operation.nop)(first_number, second_number)}")
