from datetime import date
n = int(input())
my_dates = []
for _ in range(n):
    year, month, day = input().split('-')
    my_date = date(int(year), int(month), int(day))
    my_dates.append(my_date)
my_dates = sorted(my_dates)
for date in my_dates:
    print(date.strftime('%d/%m/%Y'))
