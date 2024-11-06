from datetime import date, time, datetime
n = int(input())

result = {}
for _ in range(n):
    s = input().split()
    dr = datetime.strptime(s[2], '%d.%m.%Y')
    name = ' '.join(s[0:2])
    result[dr] = result.get(dr, []) + [name]
if len(result[min(result)]) < 2:
    print(min(result).strftime('%d.%m.%Y'), *result[min(result)])
else:
    print(min(result).strftime('%d.%m.%Y'), len(result[min(result)]))
