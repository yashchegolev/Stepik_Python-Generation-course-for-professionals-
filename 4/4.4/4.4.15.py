import json
from datetime import datetime
with open('4.4.15_food_services.json', 'r', encoding='utf-8', newline='') as food_services_file:
    data = json.load(food_services_file)
    '''
    print(*data, sep='\n')
    '''
    district_qty = {}
    name_object_qty = {}
    
    for line in data:
        district_qty[line['District']] = district_qty.get(line['District'], 0) + 1
        if line['OperatingCompany'] != '':
            name_object_qty[line['OperatingCompany']] = name_object_qty.get(line['OperatingCompany'], 0) + 1 
    print(max(district_qty, key=lambda x: district_qty[x]), ': ', district_qty[max(district_qty, key=lambda x: district_qty[x])], sep='')      
    print(max(name_object_qty, key=lambda x: name_object_qty[x]), ': ', name_object_qty[max(name_object_qty, key=lambda x: name_object_qty[x])], sep='')   
