# внутренняя логика
# класс всех исключений
#from __future__ import print_function

import random
from random import seed
import sys


class Error(Exception):
    def __init__(self, text):
        self.text = text

class BoardException(Exception):
    def __str__(self):
        return "Корабль не добавить"

# класс точек
class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Dot):
            return (self.x == other.x and
                    self.y == other.y)
        return NotImplemented

class Ship:
    def __init__(self, length, start_dot, direction, lives):
        self.length = length
        self.start_dot = start_dot
        self.direction = direction
        self.lives = lives

    def dots(self):
        dots_list = []
        x,y = self.start_dot.x, self.start_dot.y
        for i in range(self.length):
            if self.direction == "ver":
                if 0 > x + i or x+i > 6  or 0 > y  or y > 6:
                    raise BoardException
                dots_list.append([x + i, y])
            else:
                if 0 > x  or x > 6 or 0 > y+i or y+i > 6:
                    raise BoardException
                dots_list.append([x, y + i])

        return dots_list

class Board:
    def __init__(self, state_list, ship_list, hid, alive_ships):
        self.state_list = state_list
        self.ship_list = ship_list
        self.hid = hid
        self.alive_ships = alive_ships

    def add_ship(self, ship):
        #attempt = 0
        valid_results=[]
        for i in range(len(self.state_list)):
            for j in range(ship.length):
                    if self.state_list[i][0] == ship.dots()[j][0] and self.state_list[i][1] == ship.dots()[j][1]:
                        if self.state_list[i][2] == "0":
                            valid_results.append(i)
                            #self.state_list[i][2] = "x"
                        else:
                            #raise Error("You cannot place your ship there!"
                            raise BoardException()
        if len(valid_results) != ship.length:
            raise BoardException()
        else:
            for count, value in enumerate(valid_results):
                self.state_list[value][2] = "x"
            return self.state_list
        #except BoardException as mr:
            #print(mr)
        #finally:
            # return self.state_list

    def contour(self):
      try:
            for i in range(len(self.state_list)):
                for j in range(len(self.state_list)):
                    if self.state_list[i][2] == "x":
                        x, y = self.state_list[i][0], self.state_list[i][1]
                        if self.state_list[j][0] == x+1 and self.state_list[j][1] == y and self.state_list[j][2] != "x":
                            self.state_list[j][2] = "c"
                        if self.state_list[j][0] == x and self.state_list[j][1] == y-1 and self.state_list[j][2] != "x":
                            self.state_list[j][2] = "c"
                        if self.state_list[j][0] == x and self.state_list[j][1] == y+1 and self.state_list[j][2] != "x":
                            self.state_list[j][2] = "c"
                        if self.state_list[j][0] == x+1 and self.state_list[j][1] == y-1 and self.state_list[j][2] != "x":
                            self.state_list[j][2] = "c"
                        if self.state_list[j][0] == x+1 and self.state_list[j][1] == y+1 and self.state_list[j][2] != "x":
                            self.state_list[j][2] = "c"
                        if self.state_list[j][0] == x-1 and self.state_list[j][1] == y and self.state_list[j][2] != "x":
                            self.state_list[j][2] = "c"
                        if self.state_list[j][0] == x-1 and self.state_list[j][1] == y+1 and self.state_list[j][2] != "x":
                            self.state_list[j][2] = "c"
                        if self.state_list[j][0] == x-1 and self.state_list[j][1] == y-1 and self.state_list[j][2] != "x":
                            self.state_list[j][2] = "c"
      except IndexError:
        pass
      finally:
        return self.state_list

    def print_board(self):
        board = [[" "] * 6 for i in range(1,7)]
        if not self.hid:
            for i in range(len(self.state_list)):
                    x, y = self.state_list[i][0], self.state_list[i][1]
                    if self.state_list[i][2] == "x":
                        board[x-1][y-1] = "■"
                    else:
                        board[x-1][y-1] = "О"
            print()
            print("    | 1 | 2 | 3 | 4 | 5 | 6 |")
            print("  --------------------------- ")
            for i, row in enumerate(board):
                row_str = f"  {i+1} | {' | '.join(row)} | "
                print(row_str)
                print("  --------------------------- ")
            print()
        else:
            print("No board to print, sorry")

    def out(self, dot):
        if dot.x < 1 or dot.x > 6 or dot.y < 1 or dot.y > 6:
            return True
        else:
            return False

    def shoot(self, dot):
        result = ""
        try:
            if self.out(dot):
                result = "Outside"
                raise Error("Dot outside of the board!")
            for i in range(len(self.state_list)):
                if dot.x == self.state_list[i][0] and dot.y == self.state_list[i][1]:
                    if self.state_list[i][2] == "s":
                        result = "Already shot"
                        raise Error("You already shot there.")
                    if self.state_list[i][2] == "x":
                        print("You hit!")
                        self.state_list[i][2] = "s"
                        result = "Hit"
                    else:
                        print("There is empty!")
                        self.state_list[i][2] = "s"
                        result = "Empty"
        except Error as mr:
            print(mr)
        finally:
            return result

# outer logic


class Player:
    def __init__(self, own_board, foreign_board):
        self.own_board = own_board
        self.foreign_board = foreign_board

    def ask(self):
        return
        #pass

    def move(self):
        while True:
            try:
                x, y = self.ask()
                dot = Dot(x,y)
                result = self.foreign_board.shoot(dot)
                #print(result)
                if result == "Hit":
                    #print("Wow! You hit!")
                    repeat = True
                    break
                else:
                    #print(result)
                    repeat = False
                    break
            except Error:
                print("Something went wrong")
                continue
            finally:
                return repeat


class AI(Player):
    def __init__(self, own_board, foreign_board):
        super().__init__(own_board, foreign_board)

    def ask(self):
        x, y = random.randint(1,6), random.randint(1,6)
        return x, y


class User(Player):
    def __init__(self, own_board, foreign_board):
        super().__init__(own_board, foreign_board)

    def ask(self):
        while True:
            try:
                coord = input("Please, input the coordinates of the target in the format: x y : " ).split()
                x, y = coord
            except ValueError:
                print("That was not a suitable input. Please try again.")
                continue
            else:
                x, y = int(x), int(y)
                return x, y


class Game:
    def __init__(self, user, user_board, AI, AI_board):
        self.user = user
        self.user_board = user_board
        self.AI = AI
        self.AI_board = AI_board

    def random_board(self):
        state_list0 = []
        attempt=0
        for i in range(1, 7):
            for j in range(1, 7):
                state_list0.append([i, j, "0"])
        dir=["ver", "hor"]
        ships=[]
        board_0 = Board(state_list0, [], False, 6)
        while True: #and attempt < 2000:
            try:
                dot_rand = Dot(random.randint(1, 6), random.randint(1, 6))
                ship3 = Ship(3, dot_rand, random.choice(dir), 3)
                board_0.add_ship(ship3)
            except BoardException:
                attempt += 1
                continue
            else:
                #print(attempt)
                board_0.contour()
                ships.append(ship3)
                #print(len(ships))
                break
        #return board_0
        for i in range(2):
            while True:
                #if attempt > 2000:
                    #return None
                dot_rand = Dot(random.randint(1, 6), random.randint(1, 6))
                ship2 = Ship(2, dot_rand, random.choice(dir), 2)
                try:
                    board_0.add_ship(ship2)
                    board_0.contour()
                except BoardException:
                    attempt +=1
                    continue
                break
            ships.append(ship2)
        print(attempt)
        print(len(ships))
        return board_0
            #board_0.ship_list.append(ship2)
        # for i in range(4):
        #     while True:
        #         if attempt > 2000:
        #             return None
        #         dot_rand = Dot(random.randint(1, 6), random.randint(1, 6))
        #         ship1 = Ship(1, dot_rand, random.choice(dir), 1)
        #         try:
        #             board_0.add_ship(ship1)
        #         except BoardException:
        #             #print(mr)
        #             attempt += 1
        #             continue
        #         break
        #     board_0.contour()
        #     ships.append(ship1)
        # print(len(ships))
        # return board_0

game1=Game(1,1,1,1)
board = game1.random_board()
board.print_board()
# while True:
#     board = game1.random_board()
#     if board == None:
#         continue
#     else:
#         board.print_board()
# state_list0 = []
# for i in range(1, 7):
#     for j in range(1, 7):
#         state_list0.append([i, j, "0"])
# board_0 = Board(state_list0, [], False, 6)
# while True:
#     game1.random_board()
#     if game1.random_board() == None:
#         continue
#     else:
#         game1.random_board().print_board()
#         break





board = []
for x in range(0, 6):
    board.append(["0"] * 6)
#print(board)
state_list1=[]
for i in range(1,7):
    for j in range(1,7):
        state_list1.append([i,j,"0"])

dot_1 = Dot(6,4)
dot_s = Dot(6,6)
dot_s2=Dot(5,6)
ship_1 = Ship(3, dot_1, "hor", 3)
ship_2 = Ship(1, dot_s2, "ver", 1)
#print(ship_1.dots())
board_1=Board(state_list1, 1, False, 2)
#print(board_1.add_ship(ship_1))
#board_1.add_ship(ship_1)
#board_1.print_board()
#board_1.add_ship(ship_1)
#board_1.contour()
#board_1.add_ship(ship_2)
#print(board_1.contour())
#board_1.print_board()
#print(board_1.out(dot_s))
# print(board_1.shoot(dot_s))
#board_1.shoot(dot_s2)
#board_1.print_board()
#player_1 = AI(board_1, board_1)
#player_2 = User(board_1, board_1)
#print(board_1.shoot(dot_s))
#board_1.print_board()
#print(player_2.foreign_board.add_ship(ship_1))
#print(player_2.foreign_board.contour())
#print(player_2.foreign_board.shoot(dot_s))
#print(player_2.foreign_board.print_board())

#print(player_1.ask())
#player_2.ask()
#player_2.move()
#print(player_2.move())
#player_2.foreign_board.print_board()
#board_1.print_board()



















