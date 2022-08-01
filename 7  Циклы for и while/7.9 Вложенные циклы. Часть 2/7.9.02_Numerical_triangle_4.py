n = int(input())
for i in range(1, 2 * n, 2):
    for j in range(1, i + 1):
        digit = (i + 1) // 2 - abs(j - (i + 1) // 2) % n
        print(digit, end='')
    print()
