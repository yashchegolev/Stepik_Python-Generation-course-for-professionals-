x = 'abcdefghijklmnopqrstuvwxyz'
y = input()
line = input().lower()
tbl = line.maketrans(x, y)
print(line.translate(tbl))
