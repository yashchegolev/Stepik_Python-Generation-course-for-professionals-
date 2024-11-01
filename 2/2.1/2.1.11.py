def get_biggest(numbers):
    numbers = [str(num) for num in numbers]
    if len(numbers) == 0:
        return -1
    else:
        '''
        result = ''.join(sorted(numbers, reverse=True, key=lambda num: num + num * (len(max(numbers, key=len)) - len(num)) if num.count(num[0]) == len(num) else num)).lstrip('0')
        '''
        result = ''.join(sorted(numbers, reverse=True, key=lambda num: num * (len(max(numbers, key=len))))).lstrip('0')
        if result == '':          
            return 0
        else:
            return result

print(get_biggest([1, 2, 3]))
print()
print(get_biggest([61, 228, 9, 3, 11]))
print()
print(get_biggest([7, 71, 72]))
print()
print(get_biggest([]))
