def get_id(names, name):
    if type(name) != str:
        raise TypeError('Имя не является строкой') 
    elif not name.isalpha() or name != name.title():
        raise ValueError('Имя не является корректным')
    else:
        return len(names) + 1
    
names = ['Timur', 'Anri', 'Dima']
name = 'Arthur'

print(get_id(names, name))    
print()     
names = ['Timur', 'Anri', 'Dima', 'Arthur']
name = 'Ruslan1337'

try:
    print(get_id(names, name))
except ValueError as e:
    print(e)
print()     
names = ['Timur', 'Anri', 'Dima', 'Arthur', 'Ruslan']
name = ['E', 'd', 'u', 'a', 'r', 'd']

try:
    print(get_id(names, name))
except TypeError as e:
    print(e)
print()     
names = ['Timur', 'Anri', 'Dima', 'Arthur']
name = 'ruslan'

try:
    print(get_id(names, name))
except ValueError as e:
    print(e)
