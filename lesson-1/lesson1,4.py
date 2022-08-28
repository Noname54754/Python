#Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.

number = int(input('Введите целое число: '))
i = -1
while number > 10:
    last_number = number % 10
    number = number // 10
    if last_number > i:
        i = last_number
print(i)


# 892 ln = 2; number = 89; 2>-1; i=2
# 89 ln = 9; number = 8; 2 > 9; i = 9
