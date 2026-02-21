def sum_all(*args):
    print(sum(args))

sum_all(1, 2, 3)


def show_info(**kwargs):
    print(kwargs)

show_info(name="Tom", age=20)


def mixed(a, *args):
    print(a, args)

mixed(1, 2, 3, 4)


def full(a, *args, **kwargs):
    print(a, args, kwargs)

full(1, 2, 3, x=10)
