import sys
s = []
count = 0
for line in sys.stdin:
    s.append(line.strip('\n'))
    count += 1
if int(s[-1]) % 2 == 0:
    if count % 2 != 0:
        print('Анри')
    else:
        print('Дима')
else:
    if count % 2 != 0:
        print('Дима')
    else:
        print('Анри')
