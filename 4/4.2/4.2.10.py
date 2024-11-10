import csv
from datetime import datetime
with open('4.2.10_name_log.csv', 'r', encoding='utf-8', newline='') as name_log_file, open('4.2.10_new_name_log.csv', 'w', encoding='utf-8', newline='') as new_name_log_file:
    data = name_log_file.read()
    lines = sorted(data.splitlines()[1:], key=lambda line: line.split(',')[1])
    columns = data.splitlines()[0].split(',')
    '''
    print(columns)
    '''
    result = {}
    for line in lines:
        result[line.split(',')[1]] = result.get(line.split(',')[1], {})
        result[line.split(',')[1]].update({datetime.strptime(line.split(',')[2], '%d/%m/%Y %H:%M'): line.split(',')[0]})
    '''
    print(result)
    '''
    domains = [{columns[0]: result[key][max(result[key])], columns[1]: key, columns[2]: max(result[key]).strftime('%d/%m/%Y %H:%M')} for key in result]
    '''
    print(*domains, sep='\n')
    '''    
    writer = csv.DictWriter(new_name_log_file, fieldnames=columns, delimiter=',')
    writer.writeheader()                 # запись заголовков
    for domain in domains:               # запись строк
        writer.writerow(domain)  
