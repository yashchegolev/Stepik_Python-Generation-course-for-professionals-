from datetime import date, time, datetime
start = input()
next_week = []
for d in range(datetime.strptime(start, '%d.%m.%Y').toordinal() + 1, datetime.strptime(start, '%d.%m.%Y').toordinal() + 8):
    next_week.append(datetime.fromordinal(d).strftime('%d.%m'))
'''    
print(next_week)
'''
n = int(input())
result = {}
for _ in range(n):
    s = input().split()
    dr = datetime.strptime(s[2], '%d.%m.%Y')
    name = ' '.join(s[0:2])
    result[dr] = result.get(dr, []) + [name]
'''
print(result)
'''
count = 0
for d in sorted(result, reverse=True):
    if d.strftime('%d.%m') in next_week:
        print(*result[d])
        count += 1
        break
if count == 0:
    print('Дни рождения не планируются')
