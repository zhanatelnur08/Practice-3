words = ["banana", "pie", "apple"]
by_len = sorted(words, key=lambda s: len(s))
print(by_len)


pairs = [(1, 2), (3, 1), (2, 3)]
by_second = sorted(pairs, key=lambda p: p[1])
print(by_second)


nums = [-3, 1, -2, 4]
by_abs = sorted(nums, key=lambda x: abs(x))
print(by_abs)


students = [{"name": "Tom", "age": 20}, {"name": "Ann", "age": 18}]
by_age = sorted(students, key=lambda s: s["age"])
print(by_age)
