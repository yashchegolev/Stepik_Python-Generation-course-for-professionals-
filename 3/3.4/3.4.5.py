from datetime import timedelta, datetime
delta = datetime.strptime(input(), '%H:%M:%S') + timedelta(seconds=int(input()))
print(delta.strftime('%H:%M:%S'))
