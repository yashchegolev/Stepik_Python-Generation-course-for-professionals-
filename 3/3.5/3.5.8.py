# Функция из задачи 2.1.10, которая подбирает правильное окончание существиельного исходя из впереди идущего числа (1, 2, 5)
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
####################################################################################################################
# Решение задачи 
from datetime import date, time, datetime, timedelta
date_release =  datetime(2022, 11, 8, 12, 0)
today = datetime.strptime(input(), '%d.%m.%Y %H:%M')
delta = date_release - today
'''
print(date_release, today)
print()
print(delta)
'''
if date_release > today:
    if delta > timedelta(days=1) and today.strftime('%H:%M') != '12:00':
        print('До выхода курса осталось:', choose_plural(delta.days, ('день', 'дня', 'дней')), 'и', choose_plural(delta.seconds % 86400 // 3600, ('час', 'часа', 'часов')))
    elif delta > timedelta(days=1) and today.strftime('%H:%M') == '12:00':
        print('До выхода курса осталось:', choose_plural(delta.days, ('день', 'дня', 'дней')))

    elif timedelta(hours=1) <= delta < timedelta(days=1) and today.strftime('%M') != '00':
        print('До выхода курса осталось:', choose_plural(delta.seconds // 3600, ('час', 'часа', 'часов')), 'и', choose_plural(delta.seconds % 3600 // 60, ('минута', 'минуты', 'минут')))
    elif timedelta(hours=1) <= delta < timedelta(days=1) and today.strftime('%M') == '00':
        print('До выхода курса осталось:', choose_plural(delta.seconds // 3600, ('час', 'часа', 'часов')))    
    
    elif timedelta(hours=1) > delta:
        print('До выхода курса осталось:', choose_plural(delta.seconds // 60, ('минута', 'минуты', 'минут')))
else:
    print('Курс уже вышел!')
