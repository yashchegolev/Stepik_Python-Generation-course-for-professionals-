def print_bar_chart(data, mark):
    from collections import Counter
    bar_chart = Counter(data)
    max_len = len(max(bar_chart, key=lambda x: len(x)))
    '''
    print(max_len)
    '''
    for row in bar_chart.most_common():
        symbol, count = row
        print(f'{symbol}{" " * (max_len - len(symbol))} |{mark*count}')
        
        
print_bar_chart('beegeek', '+')

languages = ['java', 'java', 'python', 'C++', 'assembler', 'java', 'C++', 'C', 'pascal', 'C++', 'pascal', 'java']
print()
print_bar_chart(languages, '#')
