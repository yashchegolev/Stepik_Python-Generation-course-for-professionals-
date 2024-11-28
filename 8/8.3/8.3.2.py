def f(n):
    if n // 10 == 0:
        return n 
    else:
        return n % 10 + f(n // 10)

n = int(input())
print(f(n))
