from datetime import date
import calendar
year = int(input())
for m in range(1, 13):
    count = 0
    day_start = date(year, m, 1)
    day_end = date(year, m, calendar.monthrange(year, m)[1])
    for d in range(day_start.toordinal(), day_end.toordinal() + 1):
        if date.fromordinal(d).weekday() == 3:
            count += 1
            if count == 3:
                print(date.fromordinal(d).strftime('%d.%m.%Y'))
