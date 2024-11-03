from datetime import date
def get_date_range(start, end):
    s = []
    if start.toordinal() > end.toordinal():
        return s
    else:
        for d in range(start.toordinal(), end.toordinal() + 1):
            s.append(date.fromordinal(d))
        return s

date1 = date(2021, 10, 1)
date2 = date(2021, 10, 5)    
print(*get_date_range(date1, date2), sep='\n')    
print() 
date1 = date(2019, 6, 5)
date2 = date(2019, 6, 5)
print(get_date_range(date1, date2))
print()
date1 = date(2019, 6, 7)
date2 = date(2019, 6, 5)
print(get_date_range(date1, date2))
