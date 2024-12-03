def convert(number):
    if number >= 0:
        return (bin(number)[2:], oct(number)[2:], hex(number)[2:].upper())
    else:
        return ('-' + bin(abs(number))[2:], '-' + oct(abs(number))[2:], '-' + hex(abs(number))[2:])

print(convert(15)) 
print()
print(convert(-24))
print()
print(convert(1))
