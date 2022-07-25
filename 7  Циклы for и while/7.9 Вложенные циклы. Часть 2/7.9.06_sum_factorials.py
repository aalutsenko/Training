# Вариант 1: без вложенного цикла
from math import *
n = int(input())
sum_factorials1 = 0
for i in range(1, n + 1):
    sum_factorials1 += factorial(i)


# Вариант 2: с вложенным циклом
sum_factorials2 = 0
f = 1
for i in range(1, n + 1):
    for j in range(i, i + 1):
        f *= j
    sum_factorials2 += f
if sum_factorials1 == sum_factorials2:
    print(sum_factorials1)