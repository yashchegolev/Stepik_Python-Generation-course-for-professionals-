from collections import Counter
books = Counter([int(num) for num in input().split()])
n = int(input())
total = 0

for _ in range(n):
    book, price = [int(num) for num in input().split()]
    if book in books and books[book] != 0:
        total += price
        books.subtract({book: 1})
        '''
        print(books)
        '''
print(total)
'''
print(books)
print(n)
'''
