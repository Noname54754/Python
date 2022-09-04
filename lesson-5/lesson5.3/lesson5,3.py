"""
4)	Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

ru_dir = {
    "One": "Один",
    "Two": "Два",
    "Three": "Три",
    "Four": "Четыре",
}

file_ru = []
with open("lesson-5/lesson5.3/lesson5,3.txt", "r") as f1:
    for i in f1:
        i = i.split(" ", 1)
        file_ru.append(ru_dir[i[0]] + " " + i[1])
    print(file_ru)

with open("lesson-5/lesson5.3/lesson5.3ru.txt", "w") as f2:
    f2.writelines(file_ru)
