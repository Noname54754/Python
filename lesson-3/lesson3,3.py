"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


def my_func(n_1, n_2, n_3):
    sum_1 = n_1 + n_2
    sum_2 = n_1 + n_3
    sum_3 = n_2 + n_3
    if sum_1 > sum_2 and sum_1 > sum_3:
        print(sum_1)
    elif sum_2 > sum_1 and sum_2 > sum_3:
        print(sum_2)
    else:
        print(sum_3)
    a = [sum_1, sum_2, sum_3]
    a.sort()
    print(a[-1])


my_func(-1, 13.2, 8)
