import sys

for line in sys.stdin:
    if line.lstrip().startswith('#') == False:
        print(line.strip('\n'))
