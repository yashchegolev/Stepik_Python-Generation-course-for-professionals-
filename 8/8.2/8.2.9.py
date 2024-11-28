def print_digits(num):
    numbers = list(str(num))
    def mes(n):
        if n < len(numbers):
            print(numbers[n])
            mes(n + 1)            
    mes(0)
    
print_digits(7953021) 
