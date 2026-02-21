nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)


nums = [-2, -1, 0, 1, 2]
positive = list(filter(lambda x: x > 0, nums))
print(positive)


words = ["a", "abc", "ab", "abcd"]
long_words = list(filter(lambda s: len(s) > 2, words))
print(long_words)


names = ["", "Tom", "", "Ann"]
non_empty = list(filter(lambda s: s, names))
print(non_empty)
