def conversion_size(size):
    if 0 <= size < 1024:
        return str(round(size)) + ' B'
    elif 1024 <= size< 1024*1024:
        return str(round(size / 1024)) + ' KB'
    elif 1024*1024 <= size < 1024*1024*1024:
        return str(round(size / 1024 / 1024)) + ' MB' 
    elif 1024*1024*1024 <= size:
        return str(round(size / 1024 / 1024 / 1024)) + ' GB'
        
from zipfile import ZipFile        
with ZipFile('desktop.zip') as zip_file:
    info = zip_file.infolist()
    for file in info:
        if file.filename.count('/') == 0:
            print(file.filename, conversion_size(file.file_size))
        elif file.filename.count('/') == 1 and '' in file.filename.split('/'):
            print(file.filename[:-1])
        elif file.filename.count('/') == 1 and '' not in file.filename.split('/'):
            print(' ', file.filename.split('/')[1], conversion_size(file.file_size))
        elif file.filename.count('/') == 2 and '' in file.filename.split('/'):
            print(' ', file.filename.split('/')[1])
        elif file.filename.count('/') == 2 and '' not in file.filename.split('/'):
            print('   ', file.filename.split('/')[2], conversion_size(file.file_size))
        elif file.filename.count('/') == 3 and '' in file.filename.split('/'):
            print('   ', file.filename.split('/')[2]) 
        elif file.filename.count('/') == 3 and '' not in file.filename.split('/'):
            print('     ', file.filename.split('/')[3], conversion_size(file.file_size)) 
