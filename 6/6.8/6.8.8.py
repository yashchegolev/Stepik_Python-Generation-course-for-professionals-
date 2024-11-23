def scrabble(symbols, word):
    from collections import Counter
    counter1 = Counter(symbols.lower())
    counter2 = Counter(word.lower())
    if counter1 >= counter2:
        return True
    else:
        return False
    
print(scrabble('bbbbbeeeeegggggggeeeeeekkkkk', 'Beegeek'))   
print(scrabble('begk', 'beegeek'))
print(scrabble('beegeek', 'beegeek'))
