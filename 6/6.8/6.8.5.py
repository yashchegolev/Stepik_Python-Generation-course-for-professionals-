import sys
from collections import Counter

words = {}
for line in sys.stdin:
    words[line.strip().split()[0]] = int(line.strip().split()[1])
result = Counter(words)
'''
print(words)
print(result.most_common())
'''
print(result.most_common()[-2][0])
