from datetime import date, time

# Функция на анализ корректности из предыдущего урока
def is_correct(day, month, year):
    try:
        my_date = date(year, month, day)
        return True
    except:      # перехватываем любую ошибку
        return False

# Решение
s = input()
count = 0
while s != 'end':
    day, month, year = [int(num) for num in s.split('.')]
    if is_correct(day, month, year) == True:
        count += 1
        print('Корректная')
    else:
        print('Некорректная')
    s = input()
print(count)
