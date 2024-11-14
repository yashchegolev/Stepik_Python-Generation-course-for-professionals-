from zipfile import ZipFile
'''
with ZipFile('test.zip') as zip_file:
    zip_file.printdir()
'''
with ZipFile('test.zip') as zip_file:
    info = zip_file.infolist()
    count = 0
    for file in info:
        if file.is_dir() != True:
            count += 1
    print(count)
