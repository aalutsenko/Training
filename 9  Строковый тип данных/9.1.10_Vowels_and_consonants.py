# На вход программе подается одна строка с буквами русского языка. Напишите программу, которая определяет количество гласных и согласных букв.
# Примечание. В русском языке 10 гласных букв (а, у, о, ы, и, э, я, ю, ё, е) и 21
# согласная буква (б, в, г, д, ж, з, й, к, л, м, н, п, р, с, т, ф, х, ц, ч, ш, щ).
# Вариант 1
s = input()
vowel_letters1 = 0
consonant_letters1 = 0
string_length = int(len(s))
for i in range(string_length):
    if s[i] in 'ауоыиэяюёеАУОЫИЭЯЮЁЕ':
        vowel_letters1 += 1
    elif s[i] in 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ':
        consonant_letters1 += 1
# print('Количество гласных букв равно', vowel_letters1)
# print('Количество согласных букв равно', consonant_letters1)

# Вариант 2
# s = input()
vowel_letters2 = 0
consonant_letters2 = 0
for c in s:
    if c in 'ауоыиэяюёеАУОЫИЭЯЮЁЕ':
        vowel_letters2 += 1
    elif c in 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ':
        consonant_letters2 += 1
# print('Количество гласных букв равно', vowel_letters2)
# print('Количество согласных букв равно', consonant_letters2)
if vowel_letters1 == vowel_letters2 and consonant_letters1 == consonant_letters2:
    print('Количество гласных букв равно', vowel_letters2)
    print('Количество согласных букв равно', consonant_letters2)