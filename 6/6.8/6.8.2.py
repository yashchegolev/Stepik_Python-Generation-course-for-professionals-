from collections import Counter
words = Counter(sorted(input().lower().split()))
print(*list(map(lambda word: word[0], filter(lambda word: word[1] == min(words.most_common(), key=lambda x: x[1])[1], words.most_common()))), sep=', ')
