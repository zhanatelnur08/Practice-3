class Counter:
    count = 0
    
    @classmethod
    def increment(cls):
        cls.count += 1

Counter.increment()
print(Counter.count)


class Math:
    @staticmethod
    def add(a, b):
        return a + b

print(Math.add(2, 3))


class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        print(self.name, "barks")

d = Dog("Rex")
d.bark()


class Circle:
    pi = 3.14
    
    def __init__(self, r):
        self.r = r
    
    def area(self):
        return Circle.pi * self.r ** 2

c = Circle(5)
print(c.area())
