def hourglass(h):
    if int((16 - h) / 4) + 1 != 4:
        print('  ' * int((16 - h) / 4), str(int((16 - h) / 4) + 1) * h, ' ' * int((16 - h) / 4), sep='')
        hourglass(h - 4) 
    print('  ' * int((16 - h) / 4), str(int((16 - h) / 4) + 1) * h, '  ' * int((16 - h) / 4), sep='')

hourglass(16) 
