def my_pow(number):
    numbers = [pair[1]**pair[0] for pair in enumerate([int(n) for n in list(str(number))], 1)]
    return sum(numbers)

print(my_pow(139))
print(my_pow(123))
print(my_pow(0))
