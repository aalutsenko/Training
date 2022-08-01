# На вход программе подается одна строка состоящая из цифр. Напишите программу, которая считает сумму цифр данной строки.
s = input()
sum_digits = 0
for i in range(0, int(len(s))):
               sum_digits += int(s[i])
print(sum_digits)