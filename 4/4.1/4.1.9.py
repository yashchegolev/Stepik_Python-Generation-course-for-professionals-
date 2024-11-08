import sys
s = []
for line in sys.stdin:
    s.append(int(line.strip('\n')))

delta_ar = s[1] - s[0]
delta_ge = s[1] / s[0]
count_ar = 1 
count_ge = 1

for i in range(1, len(s)):
    if s[i] - s[i - 1] == delta_ar:
        count_ar += 1 
for i in range(1, len(s)):        
    if s[i] / s[i - 1] == delta_ge:
        count_ge += 1

if count_ar == len(s):
    print('Арифметическая прогрессия')
elif count_ge == len(s):
    print('Геометрическая прогрессия')
else:
    print('Не прогрессия') 
