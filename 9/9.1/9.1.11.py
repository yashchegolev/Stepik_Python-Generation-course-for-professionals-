s = input()
print(*sorted(sorted(sorted(sorted(sorted(s), key=lambda b: ord(b) in range(97, 123)), key=lambda b: ord(b) in range(65, 91)), key=lambda num: num in '13579'), key=lambda num: num in '02468'), sep='')
