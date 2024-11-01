def spell(*args):
    word_dict = {}
    for arg in args:
        if arg[0].lower() not in word_dict:
            word_dict[arg[0].lower()] = word_dict.get(arg[0].lower(), len(arg))
        else:
            if word_dict[arg[0].lower()] < len(arg):
                word_dict[arg[0].lower()] = len(arg)
            
    return word_dict

words = ['Россия', 'Австрия', 'Австралия', 'РумыниЯ', 'Украина', 'КИТай', 'УЗБЕКИСТАН']
print(spell(*words))
print()
print(spell('Математика', 'История', 'химия', 'биология', 'Информатика'))
print()
words = ['fruit', 'football', 'February', 'forest', 'Family']
print(spell(*words))
