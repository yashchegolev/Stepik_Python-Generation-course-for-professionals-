import pickle
from collections import namedtuple

with open('6.4.3_data.pkl', 'rb') as file:
    Animal = namedtuple('Animal', ['name', 'family', 'sex', 'color'])
    objects = pickle.load(file)
    for obj in objects:
        for key, value in obj._asdict().items():
            print(key, ': ', value, sep='')
        print() 
