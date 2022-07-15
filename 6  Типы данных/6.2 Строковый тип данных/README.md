# Строковый тип данных

> *Здесь находятся задачи по теме "Строковый тип данных"*

## 1. Вывод текста

**Условие задачи:**  
Написать программу, которая выводит текст:  
> "Python is a great language!", said Fred. "I don't ever remember having this much fun before."  

***Примечание:*** Использовать конкатенацию строк.  

**Решение:**  

Файл [6.2.1_Text_output.py](6.2.1_Text_output.py)

```python
print('"' + 'Python is a great language!' + '"' + ', said Fred. ' + '"' + 'I ' + "don't" + ' ever remember having this much fun before.' + '"')
```
## 2. Как твоё имя?

**Условие задачи:**  
Напишите программу, которая считывает с клавиатуры две строки – имя и фамилию пользователя и выводит фразу:  
> «Hello [введенное имя] [введенная фамилия]! You just delved into Python».

**Формат входных данных:**  
На вход программе подаётся две строки (имя и фамилия), каждая на отдельной строке.  
**Формат выходных данных:**  
Программа должна вывести текст в соответствии с условием задачи.
***Примечание:*** Между `firstname` и `lastname` вставьте пробел.

**Решение:**  

Файл [6.2.2_What's Your Name.py](6.2.2_What's Your Name.py)  

```python
firstname, lastname = input(), input()
print('Hello '+ firstname + ' ' + lastname + '! You just delved into Python')  
```  
