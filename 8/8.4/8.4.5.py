def dict_travel(nested_dicts): # решил без рекурсии
    result = []
    for key in nested_dicts:
        if type(nested_dicts[key]) == int or type(nested_dicts[key]) == str:
            result.append(key + ': '+ str(nested_dicts[key]))
        else:
            for key2 in nested_dicts[key]:
                if type(nested_dicts[key][key2]) == int or type(nested_dicts[key][key2]) == str:
                    result.append(key + '.' + key2 + ': '+ str(nested_dicts[key][key2]))
                else:
                    for key3 in nested_dicts[key][key2]:
                        if type(nested_dicts[key][key2][key3]) == int or type(nested_dicts[key][key2][key3]) == str:
                            result.append(key + '.' + key2 + '.' + key3 +  ': '+ str(nested_dicts[key][key2][key3]))
                        else:
                            for key4 in nested_dicts[key][key2][key3]:
                                if type(nested_dicts[key][key2][key3][key4]) == int or type(nested_dicts[key][key2][key3][key4]) == str:
                                    result.append(key + '.' + key2 + '.' + key3 + '.' + key4 + ': '+ str(nested_dicts[key][key2][key3][key4])) 
    print(*sorted(result), sep='\n')    
    
data = {'b': {'c': 30, 'a': 10, 'b': {'d': 40, 'e': 50}}}    
dict_travel(data)    
