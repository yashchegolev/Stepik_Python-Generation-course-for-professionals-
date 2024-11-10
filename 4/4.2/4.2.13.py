with open('4.2.13_prices.csv', 'r', encoding='utf-8', newline='') as file:
    data = file.read()
    lines = data.splitlines()[1:]
    columns = data.splitlines()[0].split(';')[1:]
    '''
    print(columns)
    '''
    min_price = max([int(num) for num in lines[0].split(';')[1:]])
    '''
    print(min_price)
    '''
    for line in lines:
        for i in range(len(line.split(';')[1:])):            
            if int(line.split(';')[1:][i]) <= min_price:
                min_price = int(line.split(';')[1:][i])
                product = columns[i]
                shop = line.split(';')[0]
    print(product, ': ', shop, sep='') 
