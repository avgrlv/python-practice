import math
from functools import reduce
from operator import mul

from first.calculator import CalculatorTask


def task_1_1():
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


def task_2_1():
    task = CalculatorTask()
    a, b, op = int(input('Введите первое число: ')), \
        int(input('Введите второе число: ')), \
        input(task.print_operations())
    task.calculate(a, b, op)


def task_3_1():
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


def task_4_1():
    while True:
        try:
            r_1, r_2 = float(input("Введите сопротивление резистора R1: ")), \
                float(input("Введите сопротивление резистора R2: "))
            break
        except:
            print("Введено не число!")
    print(f"Общее сопротивление цепи ={round(r_1 + r_2, 1)}")


def task_5_1():
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


def task_6_1():
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


def task_7_1():
    a = int(input("Введите целое число: "))
    sum, multiply = 0, 1
    while a > 0:
        digit = a % 10
        sum += digit
        multiply *= digit
        a = a // 10
    print(f"Сумма цифр: {sum} , произведение цифр: {multiply}")


def task_8_1():
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


def task_9_1():
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


def task_10_1():
    football_team = input("Введите название команды:")
    print(f"{football_team} - чемпион!")
    print("-" * len(football_team))
    print(football_team.lower())
    print(f"Наличие буквы 'п': {'п' in football_team.lower()}")
    print(f"Количество буквы 'а': {football_team.lower().count('а')}")


def task_11_1():
    print(f"Государство - {input('Введите государство:')}, столица - {input('Введите столицу государства:')}")


def task_12_1():
    s = "объектно-ориентированный"
    print(s[0:6])
    print(s[9:17])
    print(s[14:17])
    print(s[4:15:5])  # кот
    print("fffff")  # рента


def task_13_1():
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

def task_14_1():
    # В данной задаче все значения задаются в коде (без input())

    # 1. Создание словаря
    # Создать пустой словарь
    info = dict()

    # Добавить значения для ключей "фио", "дата_рождения", "место_рождения"
    info["фио"] = "Горлов Артём Викторович"
    info["дата_рождения"] = "07-02-1998"
    info["место_рождения"] = "Планета Земля"

    # Напечатать словарь
    print(info)

    # Создать ключ "хобби" со значением = список из строк -
    # наименований хобби (например "плавание" и т.д.)
    info["хобби"] = ["Java", "Дотка с пацанами"]

    # Добавить "программирование" в список хобби
    info["хобби"].append("программирование")

    # Создать ключ "животные" со значением = кортеж из строк -
    # имен домашних животных (например "кошка Мурка" и т.д.)
    info["животные"] = ("кошка Муся", "пёсик Рэй")

    # Создать ключ "ЕГЭ" и поместить в него пустой словарь
    info["ЕГЭ"] = dict()

    # В словарь info["ЕГЭ"] добавить информацию о сданных экзаменах,
    # где ключ - наименование предмета, а значение - количество баллов
    info["ЕГЭ"] = {
        "Русский язык": 88,
        "Математика": 92,
        "Физика": 88,
    }
    # Добавить экзамен, который не был сдан, после чего удалить его
    info["ЕГЭ"]["История"] = 0
    del info["ЕГЭ"]["История"]

    # Создать ключ "вузы" и поместить в него пустой словарь
    info["вузы"] = dict()

    # В словарь info["вузы"] добавить информацию о вузах,
    # где ключ - аббревиатура вуза, а значение -
    # количество баллов для специальности, на которую хотели поступить
    info["вузы"] = {'МИРЭА': 240, 'МГУ': 295, 'МГТУ им. Баумана': 255}

    # 2. Вывод на экран
    print("Данные:")
    # Получившийся словарь
    print(info)

    # # Список экзаменов ЕГЭ в алфавитном порядке
    # # (используйте метод ``keys()``, преобразовав результат в кортеж)
    exams = tuple(sorted(info["ЕГЭ"].keys()))
    print("Предметы:", exams)
    # # Список вузов в алфавитном порядке
    uni = tuple(sorted(info["вузы"].keys()))
    print("Вузы:", uni)

    # 3. Ответы на вопросы
    print("\nОтветы на вопросы:")

    # Выделить имя из info["фио"]
    name = info["фио"].split(" ")[1]
    # Начинается на гласную? (True/False)
    starts_with_vowel = name[0].lower() in "аеёиоуыэюя"
    print("* мое имя начинается на гласную букву:", starts_with_vowel)

    # Выделить месяц из info["дата_рождения"]
    month = info["дата_рождения"].split("-")[1]
    # Родился зимой или летом? (True/False)
    born_in_winter_or_summer = int(month) in [1, 2, 3, 6, 7, 8, 12]
    print("* родился летом или зимой:", born_in_winter_or_summer)

    # Количество хобби и первое из них
    hobbies_count = len(info["хобби"])
    print("* у меня {} хобби, первое \"{}\"".format(hobbies_count, info["хобби"][0]))

    # Количество сданных экзаменов
    print("* после окончания школы сдавал {} экз.".format(info["ЕГЭ"].keys()))

    # Сумма баллов по экзаменам
    sum_mark = sum(info["ЕГЭ"].values())
    print("* сумма баллов = {}".format(sum_mark))

    # Максимальный балл среди сданных
    max_mark = max(info["ЕГЭ"].values())
    print("* макс. балл = {}".format(max_mark))

    # Количество вузов, в которые Вы проходите по баллам
    # Подсказка: определить, проходите Вы или нет, можно простым сравнением
    # суммы баллов с проходным баллом вуза - ``True/False``.
    # Для того, чтобы определить количество таких вузов, преобразуйте
    # сравнение в целое число (используя ``int()``) и сложите все сравниваемые вузы.
    vuz_count =  sum(int(sum_mark >= vuz_score) for vuz_score in info["вузы"].values())
    print("* кол-во вузов в которые прохожу: {}".format(vuz_count))

    # --------------
    # Пример вывода:
    #
    # {'фио': 'Иванов Иван Иванович', 'место_рождения': 'Париж',
    #  'дата_рождения': '01/09/1995'}
    # Данные:
    # {'фио': 'Иванов Иван Иванович', 'животные': ('кошка Мурка',),
    #  'вузы': {'МИРЭА': 240, 'МГУ': 295, 'МГТУ им. Баумана': 255},
    #  'хобби': ['игра на гитаре', 'туризм', 'программирование'],
    #  'ЕГЭ': {'Математика': 90, 'Информатика': 88, 'Русский язык': 67},
    #  'дата_рождения': '01/09/1995', 'место_рождения': 'Париж'}
    # Предметы: Информатика, Математика, Русский язык
    # Вузы: МГТУ им. Баумана, МГУ, МИРЭА

    # Ответы на вопросы:
    # * мое имя начинается на гласную букву: True
    # * родился летом или зимой: False
    # * у меня 3 хобби, первое "игра на гитаре"
    # * после окончания школы сдавал 3 экз.
    # * сумма баллов = 245
    # * макс. балл = 90
    # * кол-во вузов в которые прохожу: 1
