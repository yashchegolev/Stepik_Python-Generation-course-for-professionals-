from zipfile import ZipFile
from datetime import datetime
with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()
    for file in sorted(info, key=lambda x: x.filename.split('/')[-1]):
        if file.file_size != 0:
            print(file.filename.split('/')[-1])
            date = datetime.strptime(' '.join([str(num) for num in file.date_time]), '%Y %m %d %H %M %S')
            print(f'  Дата модификации файла: {date}')
            print(f'  Объем исходного файла: {file.file_size} байт(а)')
            print(f'  Объем сжатого файла: {file.compress_size} байт(а)')
            print()
