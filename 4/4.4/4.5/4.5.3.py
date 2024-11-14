from zipfile import ZipFile
with ZipFile('workbook.zip') as zip_file:
    '''
    zip_file.printdir()
    '''
    info = zip_file.infolist()
    k = 100
    for file in info:
        if file.file_size != 0 and (file.compress_size / file.file_size) * 100 < k:
            k = (file.compress_size / file.file_size) * 100
            s = file
      
print(s.filename.split('/')[-1])
