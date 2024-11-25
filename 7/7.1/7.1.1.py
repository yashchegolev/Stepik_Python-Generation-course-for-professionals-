total = 0

with open('data.txt', 'r', encoding='utf-8') as file: #1 #2
    languages = file.readlines()
    for _ in languages:
        total = total + 1 #3

print(total)
