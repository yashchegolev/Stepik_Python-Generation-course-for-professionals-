def get_id(names, name):
    if not name.isalpha():
        raise TypeError('Имя не является строкой')     
    elif name != name.title():
        raise ValueError('Имя не является корректным')
    else:
        return len(names) + 1
    
try:
    print(get_weekday(1))
except ValueError as err:
    print(err)
    print(type(err))    
print()     
try:
    print(get_weekday('hello'))
except Exception as err:
    print(err)
    print(type(err))
print()     
try:
    print(get_weekday(8))
except ValueError as err:
    print(err)
    print(type(err)) 
print()     
try:
    print(get_weekday({}))
except Exception as err:
    print(err)
    print(type(err)) 
