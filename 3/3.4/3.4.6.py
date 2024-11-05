def num_of_sundays(year):
    from datetime import date, datetime
    date_start = date(year, 1, 1)  
    date_end = date(year + 1, 1, 1)  
    return len(list(filter(lambda dd: dd if date.fromordinal(dd).weekday() == 6 else None, [d for d in range(date_start.toordinal(), date_end.toordinal())])))

print(num_of_sundays(2021))

year = 2000
print(num_of_sundays(year))

print(num_of_sundays(768))
