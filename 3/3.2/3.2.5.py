from datetime import date
my_date = []
for _ in range(2):
    year, month, day = input().split('-')
    my_date.append(date(int(year), int(month), int(day)))
my_date_min = min(my_date)   
print(my_date_min.strftime('%d-%m (%Y)'))
