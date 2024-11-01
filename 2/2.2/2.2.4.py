words = [int(num) for num in input().split()]
word_dict = {}
for word in words:
    word_dict[word] = word_dict.get(word, 0) + 1
'''
print(word_dict)
'''
for key in sorted(word_dict):
    if word_dict[key] > 1:
        print(key, end=' ')
