def caching(func):
    cache = {}

    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
            print(f"Кэширован результат для {args}")
        else:
            print(f"Использован кэшированный результат для {args}")
        return cache[key]
    return wrapper


@caching
def fibonacci(n):
    if n < 0 or n is None:
        return "Пожалуйста, введите положительное целое число."
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
