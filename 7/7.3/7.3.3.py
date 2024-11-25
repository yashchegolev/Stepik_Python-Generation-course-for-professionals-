try:
    file = open(input(), encoding='utf-8')
    try:
        text = file.read()
        print(text)
    finally:
        file.close()
except FileNotFoundError:
    print('Файл не найден')
