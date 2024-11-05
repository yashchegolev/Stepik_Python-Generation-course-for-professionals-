from datetime import timedelta, datetime
dates = [datetime.strptime(d, '%d.%m.%Y') for d in input().split()]

result = []
for i in range(len(dates) - 1):
    result.append(abs((dates[i] - dates[i + 1]).days))
print(result)
