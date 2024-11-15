import pickle
with open(input(), 'rb') as file:
        obj = pickle.load(file)
        if type(obj) == list:
            obj = list(filter(lambda x: type(x) == int, obj))
            if len(obj) == 0:
                result = 0
            else:    
                result = min(obj) * max(obj)
        elif type(obj) == dict:
            if len(obj) == 0:
                result = 0
            else:
                obj = list(filter(lambda x: type(x) == int, obj))
            result = sum(obj)
        '''
        print(result)
        '''
if result == int(input()):
    print('Контрольные суммы совпадают')
else:
    print('Контрольные суммы не совпадают')
