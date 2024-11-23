from collections import Counter
words = Counter(input().lower().split())

print(words.most_common()[0][0])
