a, b = int(input()), int(input())
number, sum_divisors = 0, 0
for i in range(a, b + 1):
    s = 0
    for j in range(1, i + 1):
        if i % j == 0:
            n = i
            s += j
    #            print('n =', n, 'делитель =', j)
    #    print('n =', n, 's =', s)
    if s >= sum_divisors and n > number:
        sum_divisors = s
        number = n
print(number, sum_divisors)
