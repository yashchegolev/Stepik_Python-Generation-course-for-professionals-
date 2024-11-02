n = int(input())
emails = set([input() for _ in range(n)])
'''
print(emails)
'''
m = int(input())
for _ in range(m):
    count = 1
    name = input()
    email = name + '@beegeek.bzz'
    if email not in emails:
        emails.add(email)
        print(email)
    else:
        while True:
            email = name + str(count)  + '@beegeek.bzz'
            if email not in emails:
                emails.add(email)
                print(email)
                break
            else:
                count += 1
