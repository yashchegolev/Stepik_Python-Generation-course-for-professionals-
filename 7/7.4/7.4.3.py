import json
try:
    file = open(input(), encoding='utf-8')
    try:
        data = json.load(file) 
        print(data)
    except:
        print('Ошибка при десериализации')
    finally:
        file.close()
except FileNotFoundError:
    print('Файл не найден')
finally:
    file.close()
