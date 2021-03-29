# class Square:
#     _side = None
#
#     def __init__(self, side):
#         self.side = side
#
#     @property
#     def side(self):
#         return self._side
#
#     @side.setter
#     def side(self, value):
#         if value > 0:
#             self._side = value
#         else:
#             raise ValueError("Side should not be 0 or negative")
#
#     @property
#     def area(self):
#          return self.side ** 2
#
#
#  # sq1 = SquareFactory.create_square(1)
#  # print(sq1.side)
#
# jane = Square(4)
# print(jane.area)

try:
    c = int(input("a: "))
    print(c)  # печатаем c = a / b если всё хорошо
except ValueError:
    print("Вы ввели неправильное число")
else:  # код в блоке else выполняется только в том случае, если код в блоке try выполнился успешно (т.е. не вылетело никакого исключения).
    print("Вы ввели правильное число")
finally:  # код в блоке finally выполнится в любом случае, при выходе из try-except
    print("Выход из программы")


