from datetime import date, datetime
date_start = date(1, 1, 1)  
date_end = date(9999, 12, 31)

result = {}
for d in range(date_start.toordinal(), date_end.toordinal() + 1):
    if date.fromordinal(d).day == 13:
        result[date.fromordinal(d).weekday()] = result.get(date.fromordinal(d).weekday(), 0) + 1
print(result)      
for key in sorted(result):
    print(result[key])
