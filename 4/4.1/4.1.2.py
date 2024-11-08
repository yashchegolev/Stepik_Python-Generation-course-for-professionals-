import sys
from datetime import datetime, timedelta
s = []
for line in sys.stdin:
    s.append(datetime.strptime(line.strip('\n'), '%Y-%m-%d'))
print((max(s) - min(s)).days)
