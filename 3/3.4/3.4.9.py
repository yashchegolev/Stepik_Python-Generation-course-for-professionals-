def fill_up_missing_dates(dates):
    from datetime import timedelta, datetime
    dates_datetime = [datetime.strptime(d, '%d.%m.%Y') for d in dates]
    result = []
    for d in range(min(dates_datetime).toordinal(), max(dates_datetime).toordinal() + 1):
        result.append(datetime.fromordinal(d).strftime('%d.%m.%Y'))        
    return result

dates = ['01.11.2021', '07.11.2021', '04.11.2021', '03.11.2021']
print(fill_up_missing_dates(dates))
print()
dates = ['01.11.2021', '04.11.2021', '09.11.2021', '15.11.2021']
print(fill_up_missing_dates(dates))
