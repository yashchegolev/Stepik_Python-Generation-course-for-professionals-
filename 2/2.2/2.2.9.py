with open('2.2.9_files.txt', 'r', encoding='utf-8') as file:
    # Создаем словарь всех возможных размерностей файлов
    bytes_dict = {'B': 1, 'KB': 2**10, 'MB': 2**20, 'GB': 2**30}
    
    # Создаем словарь всех строк из файла
    s = []
    for line in file:
        line = line.strip()
        s.append(line)
    s = sorted(s)    
    
    # Создаем множество всех расширений представленных в файле
    file_extensions = set()
    for word in s:    
        file_extensions.add(word.split()[0].split('.')[1])
    '''
    print(file_extensions)    
    '''
    #
    total = 0
    for extension in sorted(file_extensions):
        for line in s:
            if extension in line.split()[0].split('.')[1]:
                print(line.split()[0])
                total += int(line.split()[1]) * bytes_dict[line.split()[2]]
        print('----------')
        if 0 <= total < 1024:
            print('Summary:', total, 'B')
        elif 1024 <= total < 1024*1024:
            print('Summary:', round(total / 1024), 'KB')
        elif 1024*1024 <= total < 1024*1024*1024:
            print('Summary:', round(total / 1024 / 1024), 'MB')  
        elif 1024*1024*1024 <= total:
            print('Summary:', round(total / 1024 / 1024 / 1024), 'GB')             
        total = 0
        
        if sorted(file_extensions).index(extension) != len(sorted(file_extensions)) - 1:
            print() 
