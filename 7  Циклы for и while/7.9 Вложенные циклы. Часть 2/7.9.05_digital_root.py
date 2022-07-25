n = int(input())
while n//10 > 0:
    digital_root = 0
    while n//10 > 0:
        digital_root += n%10
        n //= 10
    else:
        n += digital_root
digital_root = n
print(digital_root)