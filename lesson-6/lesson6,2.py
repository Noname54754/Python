"""
Задание 2.
Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
length (длина в метрах), width (ширина в метрах).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Реализовать публичный метод расчета массы асфальта, необходимого для покрытия
всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв
метра дороги асфальтом, толщиной в 1 см * число м толщины полотна.
Массу и толщину сделать публичными атрибутами.
Проверить работу метода.
Например: 20м*5000м*25кг*0.05м = 125000 кг = 125 т
"""

class Road:

    def __init__(self, _length, _width, weight, thickness):
        self._length = _length
        self._width = _width
        self.weight = weight
        self.thickness = thickness

    def mass(self):
        a = self._length
        b = self._width
        c = self.weight
        d = self.thickness
        overall = a * b * c * d // 100
        return print(f"\nОбщая масса асфальта - {a}м * {b}м * {c}кг * {d}см =", overall, "кг",
                     "=", overall // 1000, "т")


asphalt_masses = Road(20, 5000, 25, 5)
asphalt_masses.mass()