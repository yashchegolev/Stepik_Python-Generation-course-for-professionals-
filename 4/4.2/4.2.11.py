def condense_csv(filename, id_name):
    import csv
    with open(filename, 'r', encoding='utf-8', newline='') as csv_file, open('4.2.11_condensed.csv', 'w', encoding='utf-8', newline='') as condensed_file:
        data = csv_file.read()
        lines = data.splitlines()
        columns = [id_name]
        for line in lines:
            if line.split(',')[1] not in columns:  
                columns.append(line.split(',')[1])
        '''
        return columns
        '''
        result = {}
        r = {}
        for line in lines:
            result[line.split(',')[0]] = result.get(line.split(',')[0], {})
            result[line.split(',')[0]].update({line.split(',')[1]: line.split(',')[2]})  
        '''
        return result
        '''
        condense = []
        for key in result:
            result[key].update({id_name: key})
            condense.append(result[key])
        '''
        return condense
        '''
        writer = csv.DictWriter(condensed_file, fieldnames=columns, delimiter=',')
        writer.writeheader()             # запись заголовков
        for c in condense:               # запись строк
            writer.writerow(c) 
            
condense_csv('4.2.11_data.csv', id_name='ID')
