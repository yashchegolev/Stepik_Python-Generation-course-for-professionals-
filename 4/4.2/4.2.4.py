import csv

with open('4.2.4_salary_data.csv', 'r', encoding='utf-8', newline='') as csv_file:
    data = csv_file.read()
    lines = sorted(data.splitlines()[1:])
    '''
    print(*lines, sep='\n')
    '''
    result = {}
    for line in lines:
        result[line.split(';')[0]] = result.get(line.split(';')[0], 0) + int(line.split(';')[1])   
    '''    
    print(result)
    '''
    for key in result:
        count = 0
        for line in lines:
            if key in line:
                count += 1
        result[key] = result[key] / count
    '''
    print(result) 
    '''
    print(*sorted(result, key=lambda x: result[x]), sep='\n')  
