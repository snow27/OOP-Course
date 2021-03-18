import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_x(self, new_x):
        self.x = new_x

    def set_y(self, new_y):
        self.y = new_y

    # This is distance between to points
    def distance(self, x, y):
        result = math.sqrt(math.pow((x - self.x), 2) + math.pow((y - self.y), 2))
        return result


p = Point(2, 4)
p.set_x(3)
p.set_y(5)
print(p.distance(10, 2))
