'''
def get_pow(a, n):
    if n == 0:
        return 1
    else:
        return a * get_pow(a, n - 1)

def get_fast_pow(a, n):
    if n % 2 != 0:
        return get_pow(a, n)
    else:
        if n == 0:
            return 1
        else:        
            return a ** 2 * get_fast_pow(a, n - 2)
'''
def get_fast_pow(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return get_fast_pow(a*a, n//2)
    else:
        return a * get_fast_pow(a, n - 1)  
    
print(get_fast_pow(2, 100))  
