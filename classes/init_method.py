class Person:
    def __init__(self, name):
        self.name = name

p = Person("Tom")
print(p.name)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

pt = Point(3, 4)
print(pt.x, pt.y)


class Car:
    def __init__(self, brand="Unknown"):
        self.brand = brand

c = Car()
print(c.brand)


class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

b = Book("Python", 300)
print(b.title, b.pages)
