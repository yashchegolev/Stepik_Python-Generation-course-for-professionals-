from datetime import timedelta
my_time = input().split(':')
delta = timedelta(seconds=int(my_time[2]), minutes=int(my_time[1]), hours=int(my_time[0]))
print(delta.seconds)
