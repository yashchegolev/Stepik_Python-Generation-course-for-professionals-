import sys

numbers = [line.strip() for line in sys.stdin]
'''
print(numbers)
'''
total = 0
count = 0
for num in numbers:
    try:
        if '.' in num:
            total += float(num)
        else:
            total += int(num)
    except:
        count += 1
print(total)
print(count)
