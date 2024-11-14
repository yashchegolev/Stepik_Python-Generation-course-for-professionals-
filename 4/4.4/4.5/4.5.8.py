def extract_this(zip_name, *args):
    from zipfile import ZipFile
    with ZipFile(zip_name) as zip_file:
        if len(args) == 0:
            zip_file.extractall()
        else:
            for arg in args:
                zip_file.extract(arg)
                
extract_this('files.zip', 'Iurii1.txt')
