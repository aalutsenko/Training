counter = 0
a, b = int(input()), int(input())
for i in range(a, b + 1):
    if pow(i, 3) % 10 == 4 or pow(i, 3) % 10 == 9:
        counter += 1
print(counter)
