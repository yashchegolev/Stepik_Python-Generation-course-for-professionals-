from collections import Counter

data = Counter('aksjaskfjsklfjdslkfjajfopewtoieqpwdpqworiiqjskanvmcxbmpewrqopkqwlmdzczmxvmvlnjpjqpkqzxvmbowiqeorewi')
'''
symbols = Counter(data)
print(symbols)
print(symbols.most_common())
'''
def min_values():
    symbols = Counter(data)
    result = []
    for symbol in symbols.most_common():
        if symbol[1] == min(symbols.most_common(), key=lambda x: x[1])[1]:
            result.append(symbol)
    return result      
            
data.min_values = min_values
'''
print(data.min_values()) 
'''

def max_values():
    symbols = Counter(data)
    result = []
    for symbol in symbols.most_common():
        if symbol[1] == max(symbols.most_common(), key=lambda x: x[1])[1]:
            result.append(symbol)
    return result      
            
data.max_values = max_values
'''
print(data.max_values()) 
'''
