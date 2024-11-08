import sys
s = []
for line in sys.stdin:
    s.append(line.strip('\n'))

s_new = s[:-1]

result = map(lambda line: line.split(' / ')[0], sorted(sorted(filter(lambda line: line if line.split(' / ')[1] == s[-1] else None, s_new)), key=lambda line: line.split(' / ')[2]))
print(*result, sep='\n')
