"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

my_file = open("lesson-5/lesson5.2/lesson5,2.txt", "r")
k = 0
for i in my_file.readlines():
    if i != "\n":
        w = len(i.split(" "))
        k += 1
        print(f"{k}-ая строка, слов: {w}")
print(f"Всего строк: {k}")
my_file.close()