class Dog:
    pass

d = Dog()
print(d)


class Cat:
    name = "Tom"

c = Cat()
print(c.name)


class Bird:
    def fly(self):
        print("Flying")

b = Bird()
b.fly()


class Fish:
    color = "gold"
    def swim(self):
        print("Swimming")

f = Fish()
print(f.color)
f.swim()
