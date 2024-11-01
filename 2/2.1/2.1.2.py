def same_parity(numbers):
    numbers_new = list(filter(lambda num: num % 2 == numbers[0] % 2, numbers))
    return numbers_new

print(same_parity([]))
print(same_parity([6, 0, 67, -7, 10, -20]))
print(same_parity([-7, 0, 67, -9, 70, -29, 90]))
