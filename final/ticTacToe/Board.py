from final.ticTacToe.Cell import Cell


class Board:
    def __init__(self):
        self.cells = [Cell(i) for i in range(1, 10)]

    def display(self):
        for i in range(0, 9, 3):
            row = [str(cell) for cell in self.cells[i:i+3]]
            print('|'.join(row))
            if i < 6:
                print('-' * 5)

    def is_end(self):
        return all(cell.value != ' ' for cell in self.cells)

    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Горизонтальные линии
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Вертикальные линии
            (0, 4, 8), (2, 4, 6)              # Диагонали
        ]

        for combo in winning_combinations:
            values = [self.cells[i].value for i in combo]
            if all(v == values[0] and v != ' ' for v in values):
                return True
        return False