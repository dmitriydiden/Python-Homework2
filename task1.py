'''
Задача №1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
Пример:
- 6782 -> 23
- 0,56 -> 11
'''

number = input()

def summa(x):
    sum = 0
    for i in x:
       if i.isdigit():
        sum += int(i)
    print(x, "->", sum)
summa(number)
