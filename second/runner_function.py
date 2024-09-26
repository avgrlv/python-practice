def task_1_2():
    a = [1, 5, 3]
    b = [1, 5, 1, 5]
    c = [1, 3, 1, 5, 3, 3]
    print("Результат работы программы:")
    a.extend(b)
    print("Кол-во цифр 5 при первом объединении:{}".format(a.count(5)))
    while 5 in a:
        a.remove(5)
    a.extend(c)
    print("Кол-во цифр 3 при втором объединении: {}".format(a.count(3)))
    print("Итоговый список: {}".format(a))


def task_2_2():
    pass


def task_2_3():
    shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], ['педаль', 100], ['седло', 1500], ['рама', 12000],
            ['обод', 2000], ['шатун', 200], ['седло', 2700]]
    product_name = input("Введите название детали:").lower()
    product_prices = [item[1] for item in shop if item[0] == product_name]
    print(f"Количество деталей: {len(product_prices)}")
    print(f"Сумма деталей: {sum(product_prices)}")


def task_2_4():
    guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
    answer = -1
    while answer < 3 & True:
        print(f"Сейчас на вечеринке {len(guests)} человек:{guests}")
        print("Что происходит на тусе?")
        answer = int(input("1. Гость пришёл\n2. Гость ушёл\n3. Пора всех гнать"))
        if answer not in [1, 2, 3]:
            print("Нет такого варианта ответа")
            answer = -1
            continue

        if answer == 3:
            print("Вечеринка закончилась, все легли спать.")
            break
        elif answer == 2:
            guest = input("Как зовут гостя?")
            if guests.count(guest) > 0:
                guests.remove(guest)
                print("Пока, {}!".format(guest))
            else:
                print("Такого гостя нет")
        else:
            if len(guests) < 6:
                guest = input("Как зовут гостя?")
                guests.append(guest)
                print(f"Добро пожаловать на тусу, {guest}!")
            else:
                print("Сори, мест нет!")
        answer = -1


def task_2_5():
    violator_songs = [
        ['World in My Eyes', 4.86],
        ['Sweetest Perfection', 4.43],
        ['Personal Jesus', 4.56],
        ['Halo', 4.9],
        ['Waiting for the Night', 6.07],
        ['Enjoy the Silence', 4.20],
        ['Policy of Truth', 4.76],
        ['Blue Dress', 4.29],
        ['Clean', 5.83]
    ]
    n = int(input("Сколько песен выбрать?"))
    new_playlist = []
    i = 1
    while i <= n:
        song_name = input("Название {}-й песни: ".format(i))
        for s in violator_songs:
            if s[0] == song_name:
                new_playlist.append(s)
        i += 1
    print("Общее время звучания песен: {} минуты".format(sum(s[1] for s in new_playlist)))


def task_2_6():
    first_list, second_list = [], []
    for i in range(3):
        first_list.append(int(input(f"Введите {i + 1}-е число для первого списка: ")))
    for i in range(7):
        second_list.append(int(input(f"Введите {i + 1}-е число для второго списка: ")))
    print("Первый список: {}".format(first_list))
    print("Второй список: {}".format(second_list))
    print("Уникальный набор: {}".format(sorted(set(first_list + second_list))))
