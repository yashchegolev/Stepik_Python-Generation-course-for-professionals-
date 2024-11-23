from collections import Counter

words = Counter(list(map(lambda word: len(word), input().split())))
'''
print(words)
print(list(words.elements()))
'''
for word in Counter(list(words.elements())[::-1]).most_common()[::-1]:
    key, value = word
    print(f'Слов длины {key}: {value}')
