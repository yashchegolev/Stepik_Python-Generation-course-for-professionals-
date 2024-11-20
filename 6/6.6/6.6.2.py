from collections import OrderedDict

data = OrderedDict({'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника', 'TypeObject': 'кафе', 'AdmArea': 'Центральный административный округ', 'District': 'район Арбат', 'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2', 'SeatsCount': '10'})

data_new = OrderedDict()
count = 1
for _ in range(len(data)):
    if count % 2 != 0:
        key, value = data.popitem(last=False)
    elif count % 2 == 0:
        key, value = data.popitem()        
    data_new[key] = value
    count += 1
print(data_new)
