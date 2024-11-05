from datetime import timedelta, datetime
date_start = datetime.strptime(input(), '%d.%m.%Y')
print(date_start.strftime('%d.%m.%Y'))
for d in range(2, 11):
    date_start += timedelta(days=d)  
    print(date_start.strftime('%d.%m.%Y'))
