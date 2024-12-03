def linear(nested_lists):
    new_list = []
    for elem in nested_lists:
        if isinstance(elem, list):
            new_list.extend(linear(elem))
        else:
            new_list.append(elem)
    return new_list

my_list = [3, [4], [5, [6, [7, 8]]]]
print(linear(my_list))

my_list = [10, 20, 30, 40, 50]
print(linear(my_list))
