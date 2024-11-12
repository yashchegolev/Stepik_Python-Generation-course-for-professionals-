import sys
import json
with open('4.4.10_countries.json', 'r', encoding='utf-8', newline='') as countries_file, open('4.4.10_religion.json', 'w', encoding='utf-8', newline='') as religion_file: 
    data = json.load(countries_file)
    
    keys = set()
    for line in data:
        keys.add(line['religion'])
    religion = {key: [] for key in keys} 
    '''
    print(keys)
    print(religion)
    '''
    for line in data:
        religion[line['religion']] = religion.get(line['religion'], 0) + [line['country']]
    '''    
    print(religion)    
    '''    
    json.dump(religion, religion_file, indent=2)
