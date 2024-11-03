from datetime import date
def print_good_dates(dates):
    my_dates = []
    for date in dates:
        if date.year == 1992 and date.month + date.day == 29:
            my_dates.append(date)
    my_dates = sorted(my_dates)
    for date in my_dates:
        print(date.strftime('%B %d, %Y'))
    

dates = [date(1992, 10, 19), date(1991, 12, 6), date(1992, 9, 20)]
print_good_dates(dates)

dates = [date(1993, 9, 15), date(2021, 11, 2), date(2000, 7, 7)]
print_good_dates(dates)
