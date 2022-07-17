m, n = int(input()), int(input())
if m%2 == 0:
    m = m - 1
else:
    m = m
for i in range(m, n-1, -2):
    print(i)