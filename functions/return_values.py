def square(n):
    return n * n

print(square(4))


def get_name():
    return "Alice"

name = get_name()
print(name)


def divide(a, b):
    return a // b, a % b

q, r = divide(10, 3)
print(q, r)


def get_list():
    return [1, 2, 3]

print(get_list())
