def is_greater(lists, number):
    result = list(map(lambda li: True if sum(li) > number else False, lists))
    return any(result)

data = [[-3, 4, 0, 1], [1, 1, -4], [0, 0], [9, 3]]
print(is_greater(data, 10))
print()
data = [[0, 0, 1], [0, 1, 0], [1, 0, 0]]
print(is_greater(data, 2))
print()
data = [[0, 1, 2], [0, 3], [1, 1, 1], [3]]
print(is_greater(data, 3))
