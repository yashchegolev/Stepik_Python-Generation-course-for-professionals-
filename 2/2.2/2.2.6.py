n = int(input())

result = set(input().split(', '))
for _ in range(n - 1):
    result = result.intersection(input().split(', '))
    
if len(result) > 0:
    print(*sorted(result), sep=', ')
else:
    print('Сериал снять не удастся')
