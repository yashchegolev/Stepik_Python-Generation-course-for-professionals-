def is_correct_json(string):
    import json
    try:
        data = json.loads(string)
        return True
    except:
        return False
    
import json
from zipfile import ZipFile
with ZipFile('data.zip') as zip_file:
    info = zip_file.infolist()
    result = []
    for file in info:
        try:
            with zip_file.open(file.filename) as json_file:
                data = json_file.read().decode('utf-8')
                if is_correct_json(data) == True:
                    data = json.loads(data)
                    result.append(data)
        except:
            None

for name in sorted(sorted(result, key=lambda x: x['last_name']), key=lambda x: x['first_name']):
    if name['team'] == 'Arsenal':
        print(name['first_name'], name['last_name'])
