class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def move(self, board, cell_number):
        cell = board.cells[cell_number - 1]
        if cell.value == ' ':
            cell.value = self.symbol
            return True
        else:
            print("Эта клетка уже занята. Пожалуйста, выберите другую.")
            return False