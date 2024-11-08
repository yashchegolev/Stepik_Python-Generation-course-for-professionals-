import sys
count = 0
for line in sys.stdin:
    if line.lstrip().startswith('#'):
        count += 1
print(count)
