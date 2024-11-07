import calendar
s = input().split('-')
names = list(calendar.day_name)
print(names[calendar.weekday(int(s[0]), int(s[1]), int(s[2]))])
