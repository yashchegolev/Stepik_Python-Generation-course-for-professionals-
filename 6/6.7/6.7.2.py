def count_occurences(word, words):
    from collections import Counter
    counter = Counter(words.lower().split())
    return counter[word]
