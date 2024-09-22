from first.runner_function import task_1_1, task_6_1, task_5_1, task_4_1, task_3_1, task_2_1, task_10_1, task_9_1, task_8_1, task_7_1, task_11_1, \
    task_12_1, task_13_1, task_14_1
from second.runner_function import task_1_2


class Runner():
    def __init__(self):
        self.works = [
            HomeWork(1, tasks=[
                Task(1, lambda: task_1_1()),
                Task(2, lambda: task_2_1()),
                Task(3, lambda: task_3_1()),
                Task(4, lambda: task_4_1()),
                Task(5, lambda: task_5_1()),
                Task(6, lambda: task_6_1()),
                Task(7, lambda: task_7_1()),
                Task(8, lambda: task_8_1()),
                Task(9, lambda: task_9_1()),
                Task(10, lambda: task_10_1()),
                Task(11, lambda: task_11_1()),
                Task(12, lambda: task_12_1()),
                Task(13, lambda: task_13_1()),
                Task(14, lambda: task_14_1()),
            ]),
            HomeWork(2, tasks=[
                Task(1, lambda :task_1_2())
            ])
        ]


class HomeWork():
    def __init__(self, home_work_number, tasks):
        super().__init__()
        self.title = f"Домашнее задание №{home_work_number}"
        self.home_work_number = home_work_number
        self.tasks = tasks


class Task():
    def __init__(self, task_number, task_exec_foo):
        super().__init__()
        self.task_number = task_number
        self.title = f"Задача №{task_number}"
        self.task_exec_foo = task_exec_foo

    def __call__(self):
        self.task_exec_foo()

    def task_run(self):
        self.task_exec_foo()
