import json
from datetime import datetime
with open('4.4.16_food_services.json', 'r', encoding='utf-8', newline='') as food_services_file:
    lines = json.load(food_services_file)
    '''
    for line in sorted(lines, key=lambda x: x['SeatsCount']):
        print(line) 
    '''    
    result = {}
    for line in sorted(lines, key=lambda x: x['SeatsCount']):
        result.update({line['TypeObject']: {line['Name']: line['SeatsCount']}})
    
    for key, value in sorted(result.items()):
        print(key, ': ', *value.keys(), ', ', *value.values(), sep='')
