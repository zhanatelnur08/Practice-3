class Animal:
    def speak(self):
        print("Sound")

class Cat(Animal):
    def speak(self):
        print("Meow")

c = Cat()
c.speak()


class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2

s = Square(4)
print(s.area())


class Parent:
    def greet(self):
        print("Hi")

class Child(Parent):
    def greet(self):
        print("Hello")

c = Child()
c.greet()


class Bird:
    def move(self):
        print("Fly")

class Penguin(Bird):
    def move(self):
        print("Walk")

p = Penguin()
p.move()
