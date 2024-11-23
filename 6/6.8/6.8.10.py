import csv
import json
from collections import Counter

with open('quarter1.csv', mode='r', encoding='utf-8') as file1, open('quarter2.csv', mode='r', encoding='utf-8') as file2, open('quarter3.csv', mode='r', encoding='utf-8') as file3, open('quarter4.csv', mode='r', encoding='utf-8') as file4, open('prices.json', mode='r', encoding='utf-8') as file_json:
    quarter = {}
    rows1 = list(csv.reader(file1))[1:]
    for row in rows1:
        quarter[row[0]] = quarter.get(row[0], 0) + int(row[1]) + int(row[2]) + int(row[3])
    rows2 = list(csv.reader(file2))[1:]
    for row in rows2:
        quarter[row[0]] = quarter.get(row[0], 0) + int(row[1]) + int(row[2]) + int(row[3])
    rows3 = list(csv.reader(file3))[1:]
    for row in rows3:
        quarter[row[0]] = quarter.get(row[0], 0) + int(row[1]) + int(row[2]) + int(row[3])
    rows4 = list(csv.reader(file4))[1:]
    for row in rows4:
        quarter[row[0]] = quarter.get(row[0], 0) + int(row[1]) + int(row[2]) + int(row[3])  

    data = json.load(file_json)
'''
print(quarter)
print(data)   
'''
result = Counter({key: quarter[key] * data[key] for key in quarter})

print(result.total())  
