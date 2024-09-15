import math

from first.calculator import CalculatorTask


def task_1():
    while True:
        try:
            n = int(input('Введите натуральное число: '))
            break
        except:
            print("Введено не число!")
    if n > 0:
        print('Сумма = {0}'.format((n * (n + 1)) / 2))
    else:
        print('Необходимо положительное число')


def task_2():
    task = CalculatorTask()
    a, b, op = int(input('Введите первое число: ')), \
        int(input('Введите второе число: ')), \
        input(task.print_operations())
    task.calculate(a, b, op)


def task_3():
    while True:
        try:
            x, y, z = int(input('Введите x: ')), \
                int(input('Введите y: ')), \
                int(input('Введите z: '))
            break
        except:
            print("Введено не число!")
    f = round(
        pow((x ** 5 + 7) / (math.fabs(-6) * y), 1 / 3) / (7 - z * math.fabs(y)),
        3)
    print(f"Результат: {f}")


def task_4():
    while True:
        try:
            r_1, r_2 = float(input("Введите сопротивление резистора R1: ")), \
                float(input("Введите сопротивление резистора R2: "))
            break
        except:
            print("Введено не число!")
    print(f"Общее сопротивление цепи ={round(r_1 + r_2, 1)}")


def task_5():
    pass


def task_6():
    while True:
        try:
            v, t = int(input("Введите скорость спортсмена (км/ч): ")), \
                int(input("Введите время спортсмена (ч): "))
            break
        except:
            print("Введено не число!")
    distance_lap = 123
    distance = v * t
    lap = distance // distance_lap
    mod = distance - lap * distance_lap
    print(f"Спортсмен оставнится на отметке: {mod}")


def task_7():
    a = int(input("Введите целое число: "))
    sum, multiply = 0, 1
    while a > 0:
        digit = a % 10
        sum += digit
        multiply *= digit
        a = a // 10
    print(f"Сумма цифр: {sum} , произведение цифр: {multiply}")


def task_8():
    while True:
        try:
            a, b, c = int(input("Введите первое число: ")), \
                int(input("Введите второе число: ")), \
                int(input("Введите третье число: ")),
            break
        except:
            print("Введено не число!")
    min_number = min(a, b, c)
    max_number = max(a, b, c)
    between_number = a + b + c - max_number - min_number
    print(f"Минимальное число: {min_number}, максимальное число: {max_number}, число между максимальным и минимальным: {between_number}")


def task_9():
    while True:
        try:
            a, b = int(input("Введите первое число: ")), \
                int(input("Введите второе число: "))
            break
        except:
            print("Введено не число!")
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print(f"Первое число: {a}, второе число: {b}")
