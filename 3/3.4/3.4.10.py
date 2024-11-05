from datetime import timedelta, datetime
time_start = datetime.strptime(input(), '%H:%M')
time_end = datetime.strptime(input(), '%H:%M')

start = time_start
end = time_start + timedelta(minutes=45)
while end <= time_end:
    print(start.strftime('%H:%M'), '-', end.strftime('%H:%M'))
    start = end + timedelta(minutes=10)
    end = start + timedelta(minutes=45)
