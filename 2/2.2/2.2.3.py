s = [int(num) for num in input().split()]
number = [num for num in range(1, s[0] + 1)]
number[s[1] - 1: s[2]] = number[s[1] - 1: s[2]][::-1]
number[s[3] - 1: s[4]] = number[s[3] - 1: s[4]][::-1]
print(*number[:s[0]])
