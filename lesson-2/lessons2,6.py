l = []
while True:
    a = input('Добавить эллемент в список? Введите "да", если хотите добваить: ')
    if a.lower() != 'да':
        break
    name = input('Введите название: ')
    price = float(input('Введите цену: '))
    count = int(input('Введите количество: '))
    unit = input('Введите еденицы измерения: ')
    l.append((len(l), {'Имя': name, 'Цена': price, 'Количество': count, 'ед': unit}))

l2 = dict()
for _, item in l:
    for k, v in item.items():
        vl = l2.get(k) or []
        if v not in vl:
            vl.append(v)
        l2[k] = vl

print('Список: ', l)
print('Аналитика: ', l2)
