import json
from datetime import datetime
with open('4.4.14_exam_results.csv', 'r', encoding='utf-8', newline='') as exam_results_file, open('4.4.14_best_scores.json', 'w', encoding='utf-8', newline='') as best_scores_file:
    data = exam_results_file.read()
    lines = sorted(sorted(sorted(data.splitlines()[1:], key=lambda line: line.split(',')[2]),key=lambda line: datetime.strptime(line.split(',')[3], '%Y-%m-%d %H:%M:%S')), key=lambda line: line.split(',')[4])
    '''
    print(*lines, sep='\n')
    columns = data.splitlines()[0].split(',')
    print(columns)
    '''
    result = {}
    for line in lines:
        result.update({''.join(line.split(',')[0:2]): {'name': line.split(',')[0], 'surname': line.split(',')[1], 'best_score': int(line.split(',')[2]), 'date_and_time': line.split(',')[3], 'email': line.split(',')[4]}})
        
    '''
    print(*result.values(), sep='\n')
    '''
    json.dump([value for value in result.values()], best_scores_file, indent=3)
