# способ 1
def message():
    import sys
    data = [int(num) for num in list(map(str.strip, sys.stdin))]
    position_0 = data.index(0)
    data = data[:position_0 + 1]

    def mes(n):
        if n < len(data):
            mes(n + 1)            
            print(data[n])
    mes(0)
message()


#способ 2 (наиболее верный)
def message(n = int(input())):
    if n != 0:
        message(int(input()))
    print(n)    
message()
