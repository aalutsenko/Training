# Напишисать программу, вычисляющую значение тригонометрического выражения
#                   sin(x) + cos(x) + (tan(x))**2
# по заданному числу градусов x.
# Формат входных данных:
# На вход программе подается одно вещественное число xx измеряемое в градусах​. 
# Формат выходных данных:
# Программа должна вывести одно число – значение тригонометрического выражения.
# Тригонометрические функции принимают аргумент в радианах.
# Чтобы перевести градусы в радианы, воспользуйтесь формулой
# Модуль math содержит встроенную функцию radians(), которая переводит угол из градусов в угол в радианах.
from math import *
from re import X
x = float(input())
r = radians(x)
print(sin(r) + cos(r) + pow(tan(r), 2))