"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""


from sys import argv


def my_func(time, stavka, prem):
    return time * stavka + prem


sckript_name, time, stavka, prem = argv

print(f"ЗП: {my_func(int(time), int(stavka), int(prem))} р")
