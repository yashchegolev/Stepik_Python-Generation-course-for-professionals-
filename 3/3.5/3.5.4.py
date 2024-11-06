from datetime import date, time, datetime, timedelta
start = input()
end =  input() 
day_start = datetime.strptime(start, '%d.%m.%Y')
day_end = datetime.strptime(end, '%d.%m.%Y')

for d in range(day_start.toordinal(), day_end.toordinal() + 1):
    if (int(date.fromordinal(d).strftime('%d.%m.%Y').split('.')[0]) + int(date.fromordinal(d).strftime('%d.%m.%Y').split('.')[1])) % 2 != 0:
        day_start_new = d
        break
    
for d in range(day_start_new, day_end.toordinal() + 1, 3):
    if date.fromordinal(d).weekday() != 0 and date.fromordinal(d).weekday() != 3:
        print(date.fromordinal(d).strftime('%d.%m.%Y'))
