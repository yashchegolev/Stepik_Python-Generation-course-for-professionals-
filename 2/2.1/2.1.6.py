def dict_new(word):
    word_dict = {}
    for s in word:
        word_dict[s] = word_dict.get(s, 0) + 1
    return word_dict

def filter_anagrams(word, anagrams):
    word = dict_new(word)
    return list(filter(lambda s: dict_new(s) == word, anagrams))

print(filter_anagrams('отсечка', ['сеточка', 'стоечка', 'тесачок', 'чесотка']))
print(filter_anagrams('tommarvoloriddle', ['iamlordvoldemort', 'iamdevolremort', 'mortmortmortmort', 'remortvolremort']))
print(filter_anagrams('стекло', []))
