import calendar
s = input().split()
english_names = list(calendar.month_abbr)

print(calendar.month(int(s[0]), english_names.index(s[1])))
