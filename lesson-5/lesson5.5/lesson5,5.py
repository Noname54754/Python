"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

list_num = open("lesson-5/lesson5.5/lesson5,5.txt", "w")
print("Введите числа через пробелы: ")
while True:
    num = input()
    list_num.write(num + "\n")
    if num == "":
        break
list_num = open("lesson-5/lesson5.5/lesson5,5.txt", "r")
a = list_num.read().split()
k = 0
for i in a:
    k += int(i)
print("Сумма чисел в файле: ", k)
list_num.close()