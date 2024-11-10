import csv
with open('4.2.12_pystudent_counts.csv', 'r', encoding='utf-8', newline='') as file, open('4.2.12_sorted_student_counts.csv', 'w', encoding='utf-8', newline='') as sorted_file:
    data = file.read()
    lines = data.splitlines()[1:]
    columns = data.splitlines()[0].split(',')
    '''
    print(columns)
    '''
    result = []
    for line in lines:
        year = {}
        for i in range(len(line.split(','))):
            year.update({columns[i]: line.split(',')[i]})
        result.append(year) 
    '''    
    print(*result, sep='\n')    
    '''
    columns_sort = [columns[0]] + sorted(sorted(data.splitlines()[0].split(',')[1:]), key=lambda x: int(x.split('-')[0]))
    '''
    print(columns_sort) 
    '''
    writer = csv.DictWriter(sorted_file, fieldnames=columns_sort, delimiter=',')
    writer.writeheader()             # запись заголовков
    for row in result:               # запись строк
        writer.writerow(row) 
