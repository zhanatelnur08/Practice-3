class A:
    def method_a(self):
        print("A")

class B:
    def method_b(self):
        print("B")

class C(A, B):
    pass

c = C()
c.method_a()
c.method_b()


class Flyable:
    def fly(self):
        print("Flying")

class Swimmable:
    def swim(self):
        print("Swimming")

class Duck(Flyable, Swimmable):
    pass

d = Duck()
d.fly()
d.swim()


class X:
    def greet(self):
        print("X")

class Y:
    def greet(self):
        print("Y")

class Z(X, Y):
    pass

z = Z()
z.greet()


class Engine:
    power = 100

class Wheels:
    count = 4

class Car(Engine, Wheels):
    pass

car = Car()
print(car.power, car.count)
