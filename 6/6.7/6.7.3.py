from collections import Counter
counter = Counter(sorted(input().split(',')))
for key, value in sorted(counter.items()):    
    print(f'{key}: {value}')
