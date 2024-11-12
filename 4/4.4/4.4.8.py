import sys
import json
with open('4.4.8_data1.json', 'r', encoding='utf-8', newline='') as data1_file, open('4.4.8_data2.json', 'r', encoding='utf-8', newline='') as data2_file, open('4.4.8_data_merge.json', 'w', encoding='utf-8', newline='') as data_merge_file: 
    data1 = json.load(data1_file)
    data2 = json.load(data2_file) 

    data1.update(data2)

    json.dump(data1, data_merge_file, indent=2)  
