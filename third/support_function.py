import re


def count_sentences_with_digits(text):
    sentences = re.split(r'(?<=[.!?]) +', text)
    count = 0
    for sentence in sentences:
        if re.search(r'\d', sentence):
            count += 1
    return count


def draw_frame(s, k):
    length = len(s)
    border = k * (length + 2)
    framed_string = f"{k}{s}{k}"
    print(border)
    print(framed_string)
    print(border)


def character_statistics(sentence):
    sentence = sentence.lower()
    stats = {}
    for char in sentence:
        if char.isalpha() or char.isdigit():
            if char in stats:
                stats[char] += 1
            else:
                stats[char] = 1
    return stats


def crypto_caesar(text, shift):
    result = []

    for char in text:
        if 'а' <= char <= 'я':
            new_char = chr((ord(char) - ord('а') + shift) % 32 + ord('а'))
            result.append(new_char)
        elif 'А' <= char <= 'Я':
            new_char = chr((ord(char) - ord('А') + shift) % 32 + ord('А'))
            result.append(new_char)
        else:
            result.append(char)
    return ''.join(result)


def sort_numbers(*args):
    negatives = []
    non_negatives = []
    for number in args:
        if number < 0:
            negatives.append(number)
        else:
            non_negatives.append(number)
    negatives.sort(reverse=True)
    non_negatives.sort()
    return negatives, non_negatives


def is_palindrome(s):
    s = s.replace(" ", "").lower()
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


def game():
    low = 1
    high = 100
    attempts = 0
    print("Загадайте число от 1 до 100 (включительно) и ответьте на вопросы.")
    while low <= high and attempts < 7:
        mid = (low + high) // 2
        attempts += 1
        response = input(f"Твое число равно, больше или меньше {mid}? (1 — равно, 2 — больше, 3 — меньше): ")
        if response == '1':
            print(f"Ура! Я угадал число: {mid} за {attempts} попыток.")
            return
        elif response == '2':
            low = mid + 1
        elif response == '3':
            high = mid - 1
        else:
            print("Некорректный ввод. Пожалуйста, введите 1, 2 или 3.")
    print("Кажется, что-то пошло не так. Я не смог угадать число.")


digits = '0123456789ABCDEF'


def convert_to_decimal(number: str, base: int) -> int:
    decimal_value = 0
    for index, digit in enumerate(reversed(number)):
        if digit.upper() not in digits[:base]:
            raise ValueError(f"Цифра '{digit}' не допустима для системы счисления с основанием {base}.")
        decimal_value = decimal_value + digits.index(digit.upper()) * (base ** index)
    return decimal_value


def convert_from_decimal(number: int, base: int) -> str:
    if number == 0:
        return '0'
    result = []
    while number > 0:
        result.append(digits[number % base])
        number //= base
    return ''.join(reversed(result))


def find_magic_dates():
    magic_dates = []
    for year in range(1900, 2000):
        for month in range(1, 13):
            # Устанавливаем количество дней в месяце
            if month in [1, 3, 5, 7, 8, 10, 12]:
                max_days = 31
            elif month in [4, 6, 9, 11]:
                max_days = 30
            else:  # Февраль с висакосным
                max_days = 29 if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)) else 28

            for day in range(1, max_days + 1):
                if is_magic_date(day, month, year):
                    magic_dates.append(f"{day:02d}.{month:02d}.{year}")

    return magic_dates


def is_magic_date(day: int, month: int, year: int) -> bool:
    return day * month == year % 100
