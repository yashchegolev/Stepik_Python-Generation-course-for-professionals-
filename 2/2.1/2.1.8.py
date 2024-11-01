def index_of_nearest(numbers, number):
    if len(numbers) == 0:
        return -1
    else:
        return numbers.index(min(numbers, key=lambda num: abs(num - number)))

print(index_of_nearest([], 17))
print(index_of_nearest([7, 13, 3, 5, 18], 0))
print(index_of_nearest([9, 5, 3, 2, 11], 4))
print(index_of_nearest([7, 5, 4, 4, 3], 4))
