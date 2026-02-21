class Animal:
    def speak(self):
        print("Sound")

class Dog(Animal):
    pass

d = Dog()
d.speak()


class Vehicle:
    wheels = 4

class Car(Vehicle):
    pass

c = Car()
print(c.wheels)


class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    pass

s = Student("Tom")
print(s.name)


class Shape:
    color = "red"

class Circle(Shape):
    def draw(self):
        print("Circle", self.color)

c = Circle()
c.draw()
