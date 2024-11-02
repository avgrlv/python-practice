from final.ticTacToe.Board import Board
from final.ticTacToe.Player import Player


def start_game():
    board = Board()
    player1 = Player("Игрок 1", "X")
    player2 = Player("Игрок 2", "O")

    current_player = player1

    while not board.is_end():
        board.display()
        try:
            cell_number = int(input(f"{current_player.name}, выберите номер клетки (1-9): "))
            if 1 <= cell_number <= 9:
                if current_player.move(board, cell_number):
                    if board.check_winner():
                        board.display()
                        print(f"{current_player.name} победил!")
                        break
                    elif board.is_end():
                        board.display()
                        print("Ничья! На доске нет свободных клеток.")
                        break
                    else:
                        current_player = player2 if current_player == player1 else player1
                else:
                    print("Эта клетка уже занята. Пожалуйста, выберите другую.")
            else:
                print("Недопустимое значение. Введите число от 1 до 9.")
        except ValueError:
            print("Недопустимый ввод. Введите число от 1 до 9.")
