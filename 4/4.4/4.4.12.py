import sys
import json
import csv
with open('4.4.12_students.json', 'r', encoding='utf-8', newline='') as students_file, open('4.4.11_data.csv', 'w', encoding='utf-8', newline='') as data_file:
    data = json.load(students_file)
    
    result = []
    for line in data:
        if line['age'] >= 18 and line['progress'] >= 75:
            result.append({'name': line['name'], 'phone': line['phone']})
    '''  
    print(result)
    '''
    columns = ['name', 'phone']
    writer = csv.DictWriter(data_file, fieldnames=columns, delimiter=',')
    writer.writeheader()                                            # запись заголовков
    for student in sorted(result, key=lambda x: x['name']):         # запись строк
        writer.writerow(student) 
