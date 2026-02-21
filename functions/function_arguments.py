def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Tom")


def info(name, age):
    print(name, age)

info(age=25, name="Bob")


def power(base, exp=2):
    print(base ** exp)

power(3)
power(2, 4)


def show(a, b, c):
    print(a, b, c)

show(1, c=3, b=2)
