from zipfile import ZipFile
from datetime import datetime
with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()
    result = []
    for file in info:
        if file.file_size != 0 and datetime.strptime(' '.join([str(num) for num in file.date_time]), '%Y %m %d %H %M %S') > datetime(2021, 11, 30, 14, 22, 0):
            result.append(file.filename.split('/')[-1])
print(*sorted(result), sep='\n')  
