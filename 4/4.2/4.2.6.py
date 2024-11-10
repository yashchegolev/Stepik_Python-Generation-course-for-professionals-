def csv_columns(filename):
    import csv
    with open(filename, 'r', encoding='utf-8', newline='') as csv_file:
        rows = csv.DictReader(csv_file, delimiter=',', quotechar='"')
        result = {}
        for row in rows:
            for key in row:
                result[key] = result.get(key, []) + [row[key]]
        
        return result
  
print(csv_columns('exam.csv'))
