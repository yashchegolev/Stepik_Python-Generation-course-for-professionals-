import sys
import json
with open('4.4.9_people.json', 'r', encoding='utf-8', newline='') as people_file, open('4.4.9_updated_people.json', 'w', encoding='utf-8', newline='') as updated_people_file: 
    data = json.load(people_file)
    keys = set()
    for line in data:
        for key in line:
            keys.add(key)
    '''        
    print(keys)
    '''
    for line in data:
        for key in keys:
            line.setdefault(key, None)
    '''        
        print(line)        
    print(data) 
    '''
  
    json.dump(data, updated_people_file, indent=2)
