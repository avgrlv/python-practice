import math

from third.support_function import count_sentences_with_digits, draw_frame, character_statistics, crypto_caesar, \
    sort_numbers, is_palindrome, game, convert_to_decimal, convert_from_decimal, find_magic_dates


def task_3_1():
    data = list(map(int, input("Введите числа: ").split()))
    gcd = math.gcd(*data)
    lcm = math.lcm(*data)
    print(f"НОК: {gcd}, НОД:{lcm}")


def task_3_2():
    text = input("Введите текст: ")
    result = count_sentences_with_digits(text)
    print(f"Количество предложений с хотя бы одной цифрой: {result}")


def task_3_3():
    s = input("Введите строку: ")
    k = input("Введите символ для рамки: ")
    draw_frame(s, k)


def task_3_4():
    sentence = input("Введите предложение: ")
    result = character_statistics(sentence)
    for char, count in result.items():
        print(f"'{char}': {count}")


def task_3_5():
    text = input("Введите строку: ")
    shift = int(input("Введите целое число (сдвиг): "))
    encrypted = crypto_caesar(text, shift)
    print("Зашифрованная строка:", encrypted)
    decrypted = crypto_caesar(encrypted, -shift)
    print("Расшифрованная строка:", decrypted)


def task_3_6():
    result = sort_numbers(-3, 1, 4, -1, 0, -2, 5, -4)
    print("Отрицательные:", result[0])
    print("Неотрицательные:", result[1])


def task_3_7():
    user_input = input("Введите строку: ")
    if is_palindrome(user_input):
        print("Строка является палиндромом.")
    else:
        print("Строка не является палиндромом.")


def task_3_8():
    game()


def task_3_9():
    try:
        source_base = int(input("Введите исходную систему счисления (2-16): "))
        target_base = int(input("Введите целевую систему счисления (2-16): "))
        number = input("Введите число для преобразования: ")
        if source_base < 2 or source_base > 16 or target_base < 2 or target_base > 16:
            print("Ошибка: системы счисления должны быть в диапазоне от 2 до 16.")
            return
        decimal_value = convert_to_decimal(number, source_base)
        print(f"Число {number} в десятичной системе: {decimal_value}")
        converted_value = convert_from_decimal(decimal_value, target_base)
        print(f"Число {decimal_value} в системе счисления {target_base}: {converted_value}")

    except ValueError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def task_3_10():
    magic_dates = find_magic_dates()
    print("Магические даты в XX веке:")
    for date in magic_dates:
        print(date)