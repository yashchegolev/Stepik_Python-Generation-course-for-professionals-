from datetime import date, time
def is_correct(day, month, year):
    try:
        my_date = date(year, month, day)
        return True
    except:      # перехватываем любую ошибку
        return False
