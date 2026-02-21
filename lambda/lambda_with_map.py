nums = [1, 2, 3]
squared = list(map(lambda x: x ** 2, nums))
print(squared)


words = ["hi", "bye"]
upper = list(map(lambda s: s.upper(), words))
print(upper)


nums = [1, 2, 3]
doubled = list(map(lambda x: x * 2, nums))
print(doubled)


temps_c = [0, 20, 100]
temps_f = list(map(lambda c: c * 9/5 + 32, temps_c))
print(temps_f)
