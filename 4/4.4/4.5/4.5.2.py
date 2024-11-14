from zipfile import ZipFile
total_file_size = 0
total_compress_size = 0
with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()
    for file in info:
        total_file_size += file.file_size
        total_compress_size += file.compress_size        
print(f'Объем исходных файлов: {total_file_size} байт(а)')  
print(f'Объем сжатых файлов: {total_compress_size} байт(а)') 
