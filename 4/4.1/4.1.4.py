import sys
s = []
for line in sys.stdin:
    s.append(int(line.strip('\n')))
if len(s) > 0:
    print(f'Рост самого низкого ученика: {min(s)}')
    print(f'Рост самого высокого ученика: {max(s)}')
    print(f'Средний рост: {sum(s)/len(s)}')
else:
    print('нет учеников')
