from datetime import date, time, datetime, timedelta
store_opening_hours = {0: ['9:00', '21:00'], 1: ['9:00', '21:00'], 2: ['9:00', '21:00'], 3: ['9:00', '21:00'], 4: ['9:00', '21:00'], 5: ['10:00', '18:00'], 6: ['10:00', '18:00']}
s = input()
today = datetime.strptime(s, '%d.%m.%Y %H:%M')
'''
print(today.weekday())
'''
today_time = timedelta(hours=int(s.split()[1].split(':')[0]), minutes=int(s.split()[1].split(':')[1]))
'''
print(today_time)
print(timedelta(hours=int(store_opening_hours[today.weekday()][1].split(':')[0]), minutes=int(store_opening_hours[today.weekday()][1].split(':')[1])))
'''
if today_time < timedelta(hours=int(store_opening_hours[today.weekday()][0].split(':')[0]), minutes=int(store_opening_hours[today.weekday()][0].split(':')[1])) or today_time >= timedelta(hours=int(store_opening_hours[today.weekday()][1].split(':')[0]), minutes=int(store_opening_hours[today.weekday()][1].split(':')[1])):
    print('Магазин не работает')
else:
    print((timedelta(hours=int(store_opening_hours[today.weekday()][1].split(':')[0]), minutes=int(store_opening_hours[today.weekday()][1].split(':')[1])) - today_time).seconds // 60)
