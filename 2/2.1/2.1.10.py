def choose_plural(amount, declensions):
    amount_new = list(str(amount))
    amount_dict_len_1 = {0: declensions[2], 1: declensions[0], 2: declensions[1], 3: declensions[1], 4: declensions[1], 5: declensions[2], 6: declensions[2], 7: declensions[2], 8: declensions[2], 9: declensions[2]}
    if len(amount_new) == 1 and amount_new[-1] == '1' or len(amount_new) > 1 and amount_new[-1] == '1' and amount_new[-2] != '1':        
        return str(amount) + ' ' + amount_dict_len_1[int(amount_new[-1])]
    elif len(amount_new) == 1 and 2 <= int(amount_new[-1]) <= 4 or len(amount_new) > 1 and 2 <= int(amount_new[-1]) <= 4 and amount_new[-2] != '1':        
        return str(amount) + ' ' + amount_dict_len_1[int(amount_new[-1])]
    elif len(amount_new) == 1 and (int(amount_new[-1]) == 0 or 5 <= int(amount_new[-1]) <= 9) or len(amount_new) > 1 and (int(amount_new[-1]) == 0 or 5 <= int(amount_new[-1]) <= 9):        
        return str(amount) + ' ' + amount_dict_len_1[int(amount_new[-1])]
    elif 11 <= int(''.join(amount_new[-2:])) <= 14:        
        return str(amount) + ' ' + declensions[2]
    
print(choose_plural(21, ('пример', 'примера', 'примеров')))
print()
print(choose_plural(92, ('гвоздь', 'гвоздя', 'гвоздей')))
print()
print(choose_plural(8, ('яблоко', 'яблока', 'яблок')))
