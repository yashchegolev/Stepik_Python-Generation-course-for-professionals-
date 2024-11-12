import sys
import json
with open('4.4.11_playgrounds.csv', 'r', encoding='utf-8', newline='') as playgrounds_file, open('4.4.11_addresses.json', 'w', encoding='utf-8', newline='') as addresses_file:
    data = playgrounds_file.read()
    lines = data.splitlines()[1:]
    '''
    print(lines)
    '''
    result = {}
    for line in lines:
        result[line.split(';')[1]] = result.get(line.split(';')[1], {})
        result[line.split(';')[1]][line.split(';')[2]] = result[line.split(';')[1]].get(line.split(';')[2], []) + [line.split(';')[3]]
    '''
    print(result)  
    '''
    json.dump(result, addresses_file, indent=2, ensure_ascii=False)
