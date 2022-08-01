n = int(input())
fb0, fb1 = 0, 1
f = str(fb1)
for i in range(2, n + 1):
    fbi = fb0 + fb1
    f += ' ' + str(fbi)
    fb0, fb1 = fb1, fbi
print(f)
