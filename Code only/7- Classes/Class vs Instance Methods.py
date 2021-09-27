class Point:

    def draw(self):
        print(f"Point")

    def zero(cls):
        print("good")


point = Point()
# point.draw()
point = Point.zero(cls=1)
