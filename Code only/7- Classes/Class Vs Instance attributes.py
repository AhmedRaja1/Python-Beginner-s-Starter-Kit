from typing import DefaultDict


class Point:
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x},{self.y})")
        default_color = "blue"


Point.default_color = "blue"
point = Point(1, 2)
print(Point.default_color)
point.draw()

print(point.default_color)
