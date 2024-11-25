def swapcase_vowels(string):
    vowels = 'aeiouy'
    swapped_string = ''

    for char in string:
        if char in vowels: #1 ==
            swapped_string += char.upper()
        else:
            swapped_string += char
    return swapped_string #2 print()
