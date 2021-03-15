
# Greeting function
def greet():
    print("-------------------")
    print("  Приветствуем вас  ")
    print("      в игре       ")
    print("  крестики-нолики  ")
    print("-------------------")
    print(" формат ввода: 2 координаты от 0 до 2 через пробел ")


# Function for drawing playboard
def draw_board(board):
    print()
    print("    | 0 | 1 | 2 | ")
    print("  --------------- ")
    for i, row in enumerate(board):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print("  --------------- ")
    print()


# Function for taking coordinate input
def take_input():
    while True:
        coord = input("Ваш ход: ").split()

        if len(coord) != 2:
                print(" Введите 2 координаты в формате: 1 2 ")
                continue

        x, y = coord

        if not x.isdigit() or not y.isdigit():
            print(" Введите числа! ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Координаты вне диапазона! ")
            continue

        if board[x][y] is not " ":
            print(" Клетка занята! ")
            continue

        return x, y


# Function for drawing playboard
def check_win():
    win_coord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                    ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                    ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_coord:
        symbols = []
        for c in cord:
            symbols.append(board[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!")
            return True
    return False


# Play function
def main_play(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            print(" Ходит крестик!")
        else:
            print(" Ходит нолик!")
        counter += 1
        x, y = take_input()
        if counter % 2 == 1:
            board[x][y] = "X"
        else:
            board[x][y] = "0"
        if counter > 4:
            draw_board(board)
            if check_win():
                break
        if counter == 9:
            print("Победила дружба")
            break


board = [[" "] * 3 for i in range(3)]
greet()
main_play(board)
