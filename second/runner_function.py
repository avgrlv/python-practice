def task_2_2():
    first_class = list(range(160, 176, 2))
    second_class = list(range(162, 180, 3))
    full = first_class + second_class
    print(f"Первый класс: {first_class}")
    print(f"Второй класс: {second_class}")
    print(f"Смешанный: {sorted(full)}")


def task_2_3():
    shop = [['каретка', 1200],
            ['шатун', 1000],
            ['седло', 300],
            ['педаль', 100],
            ['седло', 1500],
            ['рама', 12000],
            ['обод', 2000],
            ['шатун', 200],
            ['седло', 2700]]
    product = input("Введите название детали").lower()

