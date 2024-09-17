import math
from functools import reduce
from operator import mul

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
    while True:
        try:
            a, b, m, n = float(input("Введите значение a: ")), \
                float(input("Введите значение b: ")), \
                float(input("Введите начало отрезка (m): ")), \
                float(input("Введите конец отрезка (n): "))
            break
        except:
            print("Введено не число!")
    x = -b / a
    if m <= x <= n:
        print(f"Решение уровения x = {round(x, 3)} попадает в заданный отрезок [{m};{n}]")
    else:
        print(f"Решение уровения x = {round(x, 3)} НЕ попадает в заданный отрезок [{m};{n}]")


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
    print(
        f"Минимальное число: {min_number}, максимальное число: {max_number}, число между максимальным и минимальным: {between_number}")


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


def task_10():
    football_team = input("Введите название команды:")
    print(f"{football_team} - чемпион!")
    print("-" * len(football_team))
    print(football_team.lower())
    print(f"Наличие буквы 'п': {"п" in football_team.lower()}")
    print(f"Количество буквы 'а': {football_team.lower().count("а")}")


def task_11():
    print(f"Государство - {input("Введите государство:")}, столица - {input("Введите столицу государства:")}")


def task_12():
    s = "объектно-ориентированный"
    print(s[0:6])
    print(s[9:17])
    print(s[14:17])
    print(s[4:15:5])  # кот
    print("fffff")  # рента


def task_13():
    # Создать 2 пустых списка
    a = []
    b = []

    # Добавить 2 вещественных числа (4.5 и 3.4) в список 'a' с помощью append
    a.append(4.5)
    a.append(3.4)
    # Добавить 2 вещественных числа (8.7, 1.3) в список 'a' с помощью extend
    a.extend([8.7, 1.3])
    # Добавить 2 вещественных числа (14.5, 3.4) в список 'b' с помощью append
    b.append(14.5)
    b.append(3.4)
    # Добавить 2 вещественных числа (8.7, 11.3) в список 'b'с помощью extend
    b.extend([8.7, 11.3])
    # Вставить целое число 100 на 2-е и 4-е место списка 'a'
    a.insert(1, 100)
    a.insert(3, 100)

    # Вставить целое число 200 на 1-е и 3-е место списка 'b'
    b.insert(0, 200)
    b.insert(2, 200)

    # Вывести списки на экран
    print("Исходные списки:")
    print(a)
    print(b)
    # Удалить первые элементы из списков 'a' и 'b'
    del a[0]
    del b[0]
    # Удалить элемент 100 из списка 'a'
    a.remove(100)
    # Удалить элемент 200 из списка 'b'
    b.remove(200)
    # Удалите комментарий и допишите код

    # Вывести списки на экран
    print("\nПосле удалений:")
    print(a, b)

    # Создать множества из списков 'a' и 'b', а также их пересечение
    sa = set(a)
    sb = set(b)
    sa_and_sb = sa.intersection(sb)
    # Вывести экран уникальные элементы каждого списка и общие
    print("\nУникальные элементы:")
    print(sa)
    print(sb)
    print("общие:", sa_and_sb)

    # Соединить списки 'a' и 'b'
    c = a + b
    print(c)
    # Отсортировать список 'c' по возрастанию и убыванию
    c_asc = sorted(c)
    c_desc = sorted(c, reverse=True)
    print(f"Сортировка (возр.): {c_asc} \n Сортировка (убыв.): {c_desc}")
    # Среднее арифметическое элементов списка 'c', расположенных на четных местах
    sr_ar = sum(c[::2]) / len(c[::2])
    # Среднее геометрическое элементов списка 'c', расположенных на нечетных местах
    sr_geom = (reduce(mul, c[1::2])) ** 1 / len(c[1::2])

    print(f"Среднее арифметическое: {sr_ar} \n Среднее геометрическое: {sr_geom}")

    # Максимальный и минимальный элементы
    c_max = max(c)  # Удалите комментарий и допишите код
    c_min = min(c)  # Удалите комментарий и допишите код

    print(f"max: {c_max} \n min: {c_min}")
    # Вывести результаты на экран
    print("\nИтоговые:")
    print("3-й:", c)
# --------------
# Пример вывода:
#
# Исходные списки:
# 1-й: [4.5, 100, 3.4, 100, 8.7, 1.3]
# 2-й: [200, 14.5, 200, 3.4, 8.7, 11.3]
#
# После удалений:
# 1-й: [3.4, 100, 8.7, 1.3]
# 2-й: [14.5, 3.4, 8.7, 11.3]
#
# Уникальные элементы:
# 1-й: {8.7, 1.3, 3.4, 100}
# 2-й: {8.7, 11.3, 3.4, 14.5}
# общие: {8.7, 3.4}

# Итоговые:
# 3-й: [3.4, 100, 8.7, 1.3, 14.5, 3.4, 8.7, 11.3]
# Сортировка (возр.): [1.3, 3.4, 3.4, 8.7, 8.7, 11.3, 14.5, 100]
# Сортировка (убыв.): [100, 14.5, 11.3, 8.7, 8.7, 3.4, 3.4, 1.3]
# Ср. арифм. = 29.00, ср. геометр. = 7.82
# Макс. и мин.: 100 1.3

def task_14():
    print("пока не готова")