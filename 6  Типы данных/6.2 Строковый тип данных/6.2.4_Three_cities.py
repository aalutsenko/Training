# Даны названия трех городов. Напишите программу, которая определяет самое короткое и самое длинное название города.
# Формат входных данных
# а вход программе подаётся названия трех городов, каждое на отдельной строке.
# Формат выходных данных
# Программа должна вывести самое короткое и длинное название города, каждое на отдельной строке.
# Примечание. Гарантируется, что длины названий всех трех городов различны.
city1, city2, city3 = input(), input(), input()
if len(city1) == min(len(city1), len(city2), len(city3)):
    print(city1)
    if len(city2) == max(len(city1), len(city2), len(city3)):
        print(city2)
    else: print(city3)
elif len(city2) == min(len(city1), len(city2), len(city3)):
    print(city2)
    if len(city1) == max(len(city1), len(city2), len(city3)):
        print(city1)
    else: print(city3) 
elif len(city3) == min(len(city1), len(city2), len(city3)):
    print(city3)
    if len(city1) == max(len(city1), len(city2), len(city3)):
        print(city1)
    else: print(city2)