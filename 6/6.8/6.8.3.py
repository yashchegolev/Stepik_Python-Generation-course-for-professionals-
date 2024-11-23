from collections import Counter
words = Counter(sorted(input().lower().split()))
print(max(list(map(lambda word: word[0], filter(lambda word: word[1] == max(words.most_common(), key=lambda x: x[1])[1], words.most_common())))))
