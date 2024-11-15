def filter_dump(filename, objects, typename):
    import pickle
    with open(filename, 'wb') as file:
        obj = list(filter(lambda x: type(x) == typename, objects))
        pickle.dump(obj, file) 
                
filter_dump('numbers.pkl', [1, '2', 3, 4, '5'], int) 
