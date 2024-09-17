from first.taskfunction import task_1, task_6, task_5, task_4, task_3, task_2, task_10, task_9, task_8, task_7, task_11, \
    task_12, task_13, task_14


class Runner():
    def __init__(self):
        self.works = [
            HomeWork(1, tasks=[
                Task(1, lambda: task_1()),
                Task(2, lambda: task_2()),
                Task(3, lambda: task_3()),
                Task(4, lambda: task_4()),
                Task(5, lambda: task_5()),
                Task(6, lambda: task_6()),
                Task(7, lambda: task_7()),
                Task(8, lambda: task_8()),
                Task(9, lambda: task_9()),
                Task(10, lambda: task_10()),
                Task(11, lambda: task_11()),
                Task(12, lambda: task_12()),
                Task(13, lambda: task_13()),
                Task(14, lambda: task_14()),
            ]),
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
