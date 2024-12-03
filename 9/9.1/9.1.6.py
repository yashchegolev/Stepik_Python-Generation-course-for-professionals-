#1
'''
def custom_isinstance(objects, typeinfo):
    if type(typeinfo) == tuple:
        result = list(filter(lambda obj: type(obj) in typeinfo, objects))
    else:
        result = list(filter(lambda obj: type(obj) == typeinfo, objects))
    return len(result)
'''
#2
def custom_isinstance(objects, typeinfo):
    result = [isinstance(obj, typeinfo) for obj in objects]
    return result.count(True)

numbers = [1, 'two', 3.0, 'четыре', 5, 6.0]
print(custom_isinstance(numbers, int))

numbers = [1, 'two', 3.0, 'четыре', 5, 6.0]
print(custom_isinstance(numbers, (int, float)))

numbers = [1, 'two', 3.0, 'четыре', 5, 6.0]
print(custom_isinstance(numbers, list))
