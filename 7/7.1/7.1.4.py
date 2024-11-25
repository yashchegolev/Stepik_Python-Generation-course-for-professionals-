def get_max_index(numbers):
    max_value = max(numbers)

    for index, value in enumerate(numbers, 0): 
        if value == max(numbers):
            return index
