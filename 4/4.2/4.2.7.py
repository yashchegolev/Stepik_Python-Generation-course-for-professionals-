import csv
with open('4.2.7_data.csv', 'r', encoding='utf-8', newline='') as data_file, open('4.2.7_domain_usage.csv', 'w', encoding='utf-8', newline='') as domain_usage_file:
    data = data_file.read()
    lines = data.splitlines()[1:]
    result = {}
    for line in sorted(lines, key=lambda s: s[s.find('@') + 1:]):
        result[line[line.find('@') + 1:]] = result.get(line[line.find('@') + 1:], 0) + 1
    
    columns = ['domain', 'count']
    domains = [{'domain': key, 'count': result[key]} for key in sorted(result, key=lambda x: result[x])]
        
    writer = csv.DictWriter(domain_usage_file, fieldnames=columns, delimiter=',')
    writer.writeheader()                 # запись заголовков
    for domain in domains:               # запись строк
        writer.writerow(domain)        
       
'''        
print(columns) 
print(result)
print(domains)
'''
