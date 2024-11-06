from datetime import date, time, datetime
n = int(input())

result = {}
for _ in range(n):
    s = input().split()
    dr = datetime.strptime(s[2], '%d.%m.%Y')
    name = ' '.join(s[0:2])
    result[dr] = result.get(dr, []) + [name]
'''
print(result)
print()
print(max(result.items(), key=lambda x: len(x[1])))
'''
for key, value in sorted(result.items()):
    if len(value) == len(max(result.items(), key=lambda x: len(x[1]))[1]):
        print(key.strftime('%d.%m.%Y'))
