def is_valid(string):
    if 4 <= len(string) <= 6:
        return all(map(lambda num: True if num in '0123456789' else False, string))
    else:
        return False
        
print(is_valid('92134'))
print(is_valid('89abc1'))
print(is_valid('900876'))
print(is_valid('49 83'))
