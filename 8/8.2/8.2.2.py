def numbers():
    def start(num):
        if num < 101:
            print(num)
            start(num + 1)
    start(1)
numbers() 
