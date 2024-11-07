def get_days_in_month(year, month):
    from datetime import date
    import calendar    
    english_names = list(calendar.month_name)
    day_start = date(year, english_names.index(month), 1)
    day_end = date(year, english_names.index(month), calendar.monthrange(year, english_names.index(month))[1])
    s = []
    for d in range(day_start.toordinal(), day_end.toordinal() + 1):
        s.append(date.fromordinal(d))
    return s


print(get_days_in_month(2021, 'December'))
