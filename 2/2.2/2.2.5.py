from functools import reduce
n = int(input())
number = [str(i) for i in range(1, n + 1)]
'''
print(number)
'''
word_dict = {}
for word in number:
    word_dict[str(reduce(lambda x, y: int(x) + int(y), word, 0))] = word_dict.get(str(reduce(lambda x, y: int(x) + int(y), word, 0)), 0) + 1
'''
print(word_dict)
'''
print(max(word_dict.values()))
