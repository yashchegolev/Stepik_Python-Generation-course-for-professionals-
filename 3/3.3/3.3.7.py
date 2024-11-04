def dates_not_available(booked_dates):
    from datetime import date, datetime
    dates_not_available = []
    for d in booked_dates:
        try:
            booked_date = datetime.strptime(d, '%d.%m.%Y')
            dates_not_available.append(booked_date)
        except:      # перехватываем любую ошибку
            d_start = datetime.strptime(d.split('-')[0], '%d.%m.%Y')
            d_end = datetime.strptime(d.split('-')[1], '%d.%m.%Y')
            for dd in range(d_start.toordinal(), d_end.toordinal() + 1):
                dates_not_available.append(datetime.fromordinal(dd))
    return dates_not_available

def is_available_date(booked_dates, date_for_booking):
    from datetime import date, datetime
    result = []
    try:
        date_d = datetime.strptime(date_for_booking, '%d.%m.%Y')
        if date_d in dates_not_available(booked_dates):
            result.append(False)
        else:
            result.append(True)       
    except:      # перехватываем любую ошибку
        date_d_start = datetime.strptime(date_for_booking.split('-')[0], '%d.%m.%Y')
        date_d_end = datetime.strptime(date_for_booking.split('-')[1], '%d.%m.%Y')
        result = list(map(lambda date_d: False if datetime.fromordinal(date_d) in dates_not_available(booked_dates) else True, [d for d in range(date_d_start.toordinal(), date_d_end.toordinal() + 1)]))
            
    return all(result)


dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '01.11.2021'
print(is_available_date(dates, some_date))
print()
dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '01.11.2021-04.11.2021'
print(is_available_date(dates, some_date))
print()
dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '06.11.2021'
print(is_available_date(dates, some_date))
