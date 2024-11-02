from final.FibinacciCahce import fibonacci
from final.LRUCache import LRUCache


def lru_cache_demo():
    cache = LRUCache(3)

    # Добавляем элементы в кэш
    cache.cache = ("key1", "value1")
    cache.cache = ("key2", "value2")
    cache.cache = ("key3", "value3")

    # # Выводим текущий кэш
    cache.print_cache()  # key1 : value1, key2 : value2, key3 : value3

    # Получаем значение по ключу
    print(cache.get("key2"))  # value2

    # Добавляем новый элемент, превышающий лимит capacity
    cache.cache = ("key4", "value4")

    # Выводим обновлённый кэш
    cache.print_cache()


def fib_with_cache():
    try:
        n = int(input("Введите номер числа Фибоначчи: "))
        result = fibonacci(n)
        print(f"Число Фибоначчи с номером {n}: {result}")

    except ValueError:
        print("Пожалуйста, введите целое число.")

