import sys
import json
import csv
from datetime import time
with open('4.4.13_pools.json', 'r', encoding='utf-8', newline='') as pools_file:
    data = json.load(pools_file)
    
    filter_time = list(filter(lambda pool: time(int(pool['WorkingHoursSummer']['Понедельник'].split('-')[0].split(':')[0]), int(pool['WorkingHoursSummer']['Понедельник'].split('-')[0].split(':')[1])) <= time(10, 0) and time(int(pool['WorkingHoursSummer']['Понедельник'].split('-')[1].split(':')[0]), int(pool['WorkingHoursSummer']['Понедельник'].split('-')[1].split(':')[1])) >= time(12, 0), data))
    '''
    print(*filter_time, sep='\n')
    '''
    max_length = max(map(lambda pool: pool['DimensionsSummer']['Length'], filter_time))
    '''
    print(max_length)
    '''
    result = max(filter(lambda pool: pool['DimensionsSummer']['Length'] == max_length, filter_time), key=lambda pool: pool['DimensionsSummer']['Width'])
    '''
    print(f'{result['DimensionsSummer']['Length']}x{result['DimensionsSummer']['Width']}')
    '''
    print(result['DimensionsSummer']['Length'], 'x', result['DimensionsSummer']['Width'], sep='')
    print(result['Address']) 
