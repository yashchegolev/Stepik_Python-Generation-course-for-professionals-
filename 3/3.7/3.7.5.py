import calendar
s = input().split()
english_names = list(calendar.month_name)
print(calendar.monthrange(int(s[0]), english_names.index(s[1]))[1])
