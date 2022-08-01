n = int(input())
s1 = n  # наибольшее число последовательности
s2 = 0  # второе наибольшее число последовательности
for _ in range(n):
    x = int(input())
    if x > s1 and x > s2:
        s1, s2 = x, s1
    elif s1 > x > s2:
        s2 = x
print(s1)
print(s2)
