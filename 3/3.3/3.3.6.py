with open('3.3.6_diary.txt', 'r', encoding='utf-8') as file:
    from datetime import datetime
    dates_dict = {}
    dates = []
    for line in file:
        line = line.strip()
        try:
            my_datetime = datetime.strptime(line, '%d.%m.%Y; %H:%M')
            dates.append(my_datetime)
            '''
            dates_dict.setdefault(my_datetime, [])
            '''
            dates_dict[my_datetime] = []
        except:      # перехватываем любую ошибку
            if line != '':
                dates_dict[my_datetime] = dates_dict[my_datetime] + [line]
    for key in sorted(dates_dict):
        print(key.strftime('%d.%m.%Y; %H:%M'))
        for line in dates_dict[key]:
            print(line)
        
        if sorted(dates).index(key) != len(sorted(dates)) - 1:
            print() 
        '''
        print()
        '''
