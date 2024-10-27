class Counter:
    def __init__(self, value):
        if value < 0:
            raise Exception("Значение счётчика меньше 0")
        self.cnt = value

    def get_cnt(self):
        return self.cnt

    def increment(self):
        self.cnt += 1

    def decrement(self):
        if self.cnt - 1 < 0:
            self.cnt = 0
        else:
            self.cnt -= 1
