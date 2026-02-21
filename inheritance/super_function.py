class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

d = Dog("Rex", "Husky")
print(d.name, d.breed)


class A:
    def greet(self):
        print("Hello from A")

class B(A):
    def greet(self):
        super().greet()
        print("Hello from B")

b = B()
b.greet()


class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, job):
        super().__init__(name)
        self.job = job

e = Employee("Tom", "Dev")
print(e.name, e.job)


class Base:
    def show(self):
        return "Base"

class Child(Base):
    def show(self):
        return super().show() + " + Child"

c = Child()
print(c.show())
