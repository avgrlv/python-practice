from fourth.clock import Clock
from fourth.point import Point
from fourth.rectangle import Rectangle
from fourth.zoo.grass import Grass
from fourth.zoo.herbivorous import Herbivorous
from fourth.zoo.meat import Meat


def geometry():
    left = Point("p1")
    right = Point("p2")
    if left > right:
        return print("Точка p1 больше точки p2")
    rectangle = Rectangle(left, right)
    print(rectangle)

    some_point = Point("p3")
    if rectangle.__contains__(some_point):
        print(f"Точка {some_point} находится внутри прямоугольника")
    else:
        print(f"Точка {some_point} находится за пределами прямоугольника")


def oclock():
    time = Clock()
    time.add_seconds(660)
    time.add_minutes(43)
    time.add_hours(5)
    time2 = Clock()
    time2 + time


def animal_zoo():
    cow = Herbivorous("Корова")
    foods = [Meat(), Grass()]
    while True:
        if cow.is_hungry():
            print(cow.name + ' голодает')
            for food in foods:
                cow.eat(food)
        else:
            cow.food.nutrition -= 10


def sum_numbers():
    total_sum = 0
    while True:
        user_input = input("Введите число (или оставьте пустым для выхода): ")
        if user_input == "":
            print(f"Программа завершена. Итоговая сумма: {total_sum}")
            break
        try:
            number = float(user_input)
            total_sum += number
            print(f"Текущая сумма: {total_sum}")
        except ValueError:
            print("Некорректный ввод! Пожалуйста, введите число.")


def grade_converter():
    # Таблица для перевода из числовых оценок в буквенные
    num_to_letter = {
        (91, 100): 'A',
        (84, 90): 'B',
        (74, 83): 'C',
        (68, 73): 'b',
        (61, 67): 'E',
        (0, 60): 'P'
    }

    # Таблица для перевода из буквенных оценок в числовые
    letter_to_num = {
        'A': '91-100',
        'B': '84-90',
        'C': '74-83',
        'b': '68-73',
        'E': '61-67',
        'P': '0-60'
    }

    while True:
        user_input = input("Введите оценку (буквенную или числовую) или оставьте пустым для выхода: ")
        if user_input == "":
            print("Программа завершена.")
            break
        try:
            numeric_grade = int(user_input)
            if 0 <= numeric_grade <= 100:
                for (min_val, max_val), letter in num_to_letter.items():
                    if min_val <= numeric_grade <= max_val:
                        print(f"Числовая оценка {numeric_grade} соответствует буквенной оценке: {letter}")
                        break
            else:
                print("Числовая оценка должна быть в диапазоне от 0 до 100.")
        except ValueError:
            letter_grade = user_input.upper()
            if letter_grade in letter_to_num:
                print(
                    f"Буквенная оценка {letter_grade} соответствует числовому диапазону: {letter_to_num[letter_grade]}")
            else:
                print(
                    "Некорректная оценка! Пожалуйста, введите допустимую оценку (A, B, C, D, F или число от 0 до 100).")
