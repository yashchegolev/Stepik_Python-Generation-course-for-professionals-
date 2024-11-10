with open('4.2.9_titanic.csv', 'r', encoding='utf-8', newline='') as titanic_file:
    data = titanic_file.read()
    lines = sorted(data.splitlines()[1:], key=lambda line: line.split(';')[2], reverse=True)
    '''
    print(*lines, sep='\n')
    '''
    result = list(map(lambda line: line.split(';')[1], filter(lambda line: int(line.split(';')[0]) == 1 and float(line.split(';')[3]) < 18, lines)))
    print(*result, sep='\n')
