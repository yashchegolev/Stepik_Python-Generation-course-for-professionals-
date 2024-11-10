import csv

with open('4.2.5_deniro.csv', 'r', encoding='utf-8', newline='') as csv_file:
    data = csv_file.read()
    lines = data.splitlines()
    n = int(input())
    if n <= 1:
        print(*sorted(lines, key=lambda line: line.split(',')[n - 1]), sep='\n')
    else:
        print(*sorted(lines, key=lambda line: int(line.split(',')[n - 1])), sep='\n')
