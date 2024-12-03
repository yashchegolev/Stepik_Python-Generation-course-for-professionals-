def non_negative_even(numbers):
    result = list(map(lambda num: True if num >= 0 and num % 2 == 0 else False, numbers))
    return all(result)
