count = 0
for _ in range(10):
    if int(input()) % 2 == 0:
        count += 1
if count == 10:
    print('YES')
else:
    print('NO')
