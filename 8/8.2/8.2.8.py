def print_digits(num):
    numbers = list(str(num))
    def mes(n):
        if n < len(numbers):
            mes(n + 1)            
            print(numbers[n])
    mes(0)
    
print_digits(7953021) 
