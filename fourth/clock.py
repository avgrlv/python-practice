class Clock:
    def __init__(self):
        try:
            hours = int(input("Сколько часов: "))
            minutes = int(input("Сколько минут: "))
            seconds = int(input("Сколько секунд: "))
        except (TypeError):
            print("Введено не целое число")
            raise

        total_seconds = hours * 3600 + minutes * 60 + seconds

        self.hours = (total_seconds // 3600) % 24
        self.minutes = (total_seconds % 3600) // 60
        self.seconds = total_seconds % 60
        print(f"Введенное время: {self}")

    def add_seconds(self, seconds):
        total_seconds = self.get_as_seconds() + seconds

        self.hours = (total_seconds // 3600) % 24
        self.minutes = (total_seconds % 3600) // 60
        self.seconds = total_seconds % 60
        print(f"Текущее время: {self}")

    def add_minutes(self, minutes):
        self.add_seconds(minutes * 60)

    def add_hours(self, hours):
        self.add_seconds(hours * 3600)

    def get_as_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        return self.add_seconds(other.get_as_seconds())
