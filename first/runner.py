from first.calculator import CalculatorTask


def task_2():
    task = CalculatorTask()
    a, b, op = int(input('Введите первое число: ')), \
        int(input('Введите второе число: ')), \
        input(task.print_operations())
    task.calculate(a, b, op)