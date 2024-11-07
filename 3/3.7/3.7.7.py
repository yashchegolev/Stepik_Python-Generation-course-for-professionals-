def get_all_mondays(year):
    from datetime import date
    import calendar 
    day_start = date(year, 1, 1)
    day_end = date(year, 12, 31)
    s= []
    for d in range(day_start.toordinal(), day_end.toordinal() + 1):
        if date.fromordinal(d).weekday() == 0:
            s.append(date.fromordinal(d))
    return s 


print(get_all_mondays(2021))
