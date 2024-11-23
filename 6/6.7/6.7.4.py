from collections import Counter
counter = Counter(sorted(input().split(',')))
total = 0
len_max = len(max(counter.keys(), key=lambda x: len(x)))
for key, value in sorted(counter.items()):   
    for symbol in key.replace(' ', ''):
        total += ord(symbol)
    print(f'{key}{" " * (len_max - len(key) )}: {total} UC x {value} = {total*value} UC')
    total = 0
