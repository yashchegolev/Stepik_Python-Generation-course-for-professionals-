import sys
import json
with open('4.4.7_data.json', 'r', encoding='utf-8', newline='') as file, open('4.4.7_updated_data.json', 'w', encoding='utf-8', newline='') as data_file: 
    data = json.load(file) 
    '''
    print(data)
    '''
    count = 0
    for i in range(len(data)):
        '''
        print(type(data[i]))
        '''
        if type(data[i]) == str:
            data[i] += '!'
        elif type(data[i]) == int:
            data[i] += 1
        elif type(data[i]) == bool:
            data[i] = not data[i]
        elif type(data[i]) == bool:
            data[i] = not data[i] 
        elif type(data[i]) == list:
            data[i] *= 2
        elif type(data[i]) == dict:
            data[i].update({"newkey": None})
        elif data[i] == None:
            count += 1
            
    for i in range(count):         
        data.remove(None)
    json.dump(data, data_file, indent=2) 
