# Назовем число интересным, если в нем разность максимальной и минимальной цифры равняется средней по величине цифре.
# Напишите программу, которая определяет интересное число или нет.
# Если число интересное, следует вывести – «Число интересное» иначе «Число неинтересное».
a = int(input())
d3 = a%10
d2 = (a//10)%10
d1 = a//100
if (max(d1, d2, d3) - min(d1, d2, d3)) == (d1 + d2+ d3 - max(d1, d2, d3) - min(d1, d2, d3)):
    print('Число интересное')
else:
    print('Число неинтересное')