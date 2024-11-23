import csv
from collections import Counter
emails = []
with open('6.8.7_name_log.csv', mode='r', encoding='utf-8') as name_log_file:
    rows = list(csv.reader(name_log_file))[1:]
    for row in rows:
        emails.append(row[1])
        
result = Counter(emails)
for row in sorted(result.most_common()):
    email, count = row
    print(f'{email}: {count}') 
