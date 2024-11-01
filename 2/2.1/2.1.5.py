def convert(string):
    total_a = 0
    total_A = 0
    for s in string:
        if s in 'abcdefghijklmnopqrstuvwxyz':
            total_a += 1
        elif s in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            total_A += 1
    if total_a >= total_A:
        return string.lower()
    else:
        return string.upper()
    
print(convert('BEEgeek'))
print(convert('pyTHON'))
print(convert('pi31415!'))
