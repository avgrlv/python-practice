import math

from first.calculator import CalculatorTask


def task_2():
    task = CalculatorTask()
    a, b, op = int(input('Введите первое число: ')), \
        int(input('Введите второе число: ')), \
        input(task.print_operations())
    task.calculate(a, b, op)


def task_3():
    x, y, z = int(input('Введите x: ')), \
        int(input('Введите y: ')), \
        int(input('Введите z: '))
    f = round(
        pow((x ** 5 + 7) / (math.fabs(-6) * y), 1 / 3) / (7 - z * math.fabs(y)),
        3)
    print(f"Результат: {f}")


def task_4():
    r_1, r_2 = float(input("Введите сопротивление резистора R1: ")), \
        float(input("Введите сопротивление резистора R2: "))
    print(f"Общее сопротивление цепи ={round(r_1 + r_2, 1)}")


def task_5():
    pass


def task_6():
    pass


def task_7():
    pass


def task_8():
    pass


def task_9():
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print(f"Первое число: {a}, второе число: {b}")
