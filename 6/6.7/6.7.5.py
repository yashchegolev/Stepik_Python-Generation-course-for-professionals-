from collections import Counter
with open('6.7.5_pythonzen.txt', 'r', encoding='utf-8') as file:
    pythonzen = Counter()
    for line in file.readlines():
        pythonzen.update(''.join(line.strip().lower().split(' ')))

for key, value in sorted(pythonzen.items()):
    if 97 <= ord(key) <= 122:
        print(f'{key}: {value}')
