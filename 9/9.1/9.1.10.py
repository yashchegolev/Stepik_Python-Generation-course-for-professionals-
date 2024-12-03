def zip_longest(*args, fill=None):
    len_max = max([len(arg) for arg in args])
    for arg in args:
        if len(arg) < len_max:
            for _ in range(len_max - len(arg)):
                arg.append(fill)
    return list(zip(*args))   

print(zip_longest([1, 2, 3, 4, 5], ['a', 'b', 'c'], fill='_'))

data = [[1, 2, 3, 4, 5], ['one', 'two', 'three'], ['I', 'II']]
print(zip_longest(*data))

data = [[1, 2, 3, 4, 5], ['one', 'two', 'three', 'four', 'five'], ['I', 'II', 'III', 'IV', 'V']]
print(zip_longest(*data))
