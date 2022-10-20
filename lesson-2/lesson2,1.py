"""
Задание 1. Создать список и заполнить ego элементами различных типов данных.
Реализовать проверку типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать y пользователя, a указать явно, в программе.

Пример:
для списка [5, "string", 0.15, True, None]
результат

<class 'int'>
<class 'str'>
<class 'float'>
<class 'bool'>
<class 'NoneType'>
"""

#a = [5, 'string', 0.15, True, None]
#for i in range(len(a)):
#    print(type(a[i]))
    
a = [5, 'string', 0.15, True, None]
for i in a:
    print(type(i))