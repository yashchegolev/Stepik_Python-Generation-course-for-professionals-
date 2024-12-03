def get_all_values(nested_dicts, key):
    my_set = set()
    if key in nested_dicts :
        if type(nested_dicts[key]) == int or type(nested_dicts[key]) == str:
            my_set.add(nested_dicts[key])
        else:
            my_set.update(nested_dicts[key])
        return my_set

    for v in nested_dicts.values():
        if type(v) == dict:
            for v1 in v.values():
                if type(v1) == dict:
                    value1 = get_all_values(v1, key)
                    my_set.update(value1)  
            value = get_all_values(v, key)
            my_set.update(value)   
    return my_set   

my_dict = {
           'Arthur': {'hobby': 'videogames', 'drink': 'cacao'}, 
           'Timur': {'hobby': 'math'},
           'Dima': {
                   'hobby': 'CS',
                   'sister':
                       {
                         'name': 'Anna',
                         'hobby': 'TV',
                         'age': 14
                       }
                   }
           }

result = get_all_values(my_dict, 'hobby')
print(*sorted(result))


#################################################################################################################################

my_dict = {'users': {'Arthur': {'grades': [4, 4, 3], 'top_grade': 4}, 'Timur': {'grades': [5, 5, 5], 'top_grade': 5}}}
result = get_all_values(my_dict, 'top_grade')

print(*sorted(result))
print(type(result))

my_dict = {'Arthur': {'hobby': 'videogames', 'drink': 'cacao'}, 'Timur': {'hobby': 'math'}}
result = get_all_values(my_dict, 'hobby')

print(*sorted(result))
