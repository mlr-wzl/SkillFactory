# задание 1.10.1-1.10.2

class Rectangle:
    def __init__(self, x, y, width, height):
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def __str__(self):
        return f"Rectangle({self.x}, {self.y}, {self.width}, {self.height})"

    def get_area(self):
        return self.width * self.height


rectangle_1 = Rectangle(1, 2, 5, 10)
print(rectangle_1)
print(rectangle_1.get_area())

