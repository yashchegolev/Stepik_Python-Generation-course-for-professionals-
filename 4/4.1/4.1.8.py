import sys
from datetime import datetime
s = []
for line in sys.stdin:
    s.append(datetime.strptime(line.strip('\n'), '%d.%m.%Y'))
if len(s) == len(set(s)):
    if s == sorted(s):
        print('ASC')
    elif s == sorted(s, reverse=True):
        print('DESC')
    else:
        print('MIX')
else:
    print('MIX')
