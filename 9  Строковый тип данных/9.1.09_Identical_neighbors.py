# На вход программе подается одна строка. Напишите программу, которая определяет сколько в ней одинаковых соседних символов.
s = input()
count = 0
symbol = s[0]
string_length = int(len(s))
for i in range(1, string_length):
    if s[i] == symbol:
        count += 1
    symbol = s[i]
print(count)