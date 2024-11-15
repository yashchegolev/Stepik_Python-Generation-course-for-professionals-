import pickle
import sys
pkl = input()      
with open(pkl, 'rb') as file:     # используется файл полученный на предыдущем шаге
    obj = pickle.load(file)
print(obj(*list(map(str.strip, sys.stdin))))
