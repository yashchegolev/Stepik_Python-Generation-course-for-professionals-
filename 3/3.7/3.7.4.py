import calendar
s = input().split()
print(calendar.monthrange(int(s[0]), int(s[1]))[1])
