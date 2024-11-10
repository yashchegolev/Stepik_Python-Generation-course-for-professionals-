with open('4.2.8_wifi.csv', 'r', encoding='utf-8', newline='') as wifi_file:
    data = wifi_file.read()
    lines = sorted(data.splitlines()[1:], key=lambda line: line.split(';')[1])
    result = {}
    for line in lines:
        result[line.split(';')[1]] = result.get(line.split(';')[1], 0) + int(line.split(';')[3])
    for key in sorted(result, key=lambda x: result[x], reverse=True):
        print(key, ': ', result[key], sep='')
