import math

def trapecia_area(a, b, c, d):
    # Вычисляем полупериметр
    p = (a + b + c + d) / 2
    
    # Вычисляем площадь по формуле Герона
    area = math.sqrt(p * (p - a) * (p - b) * (p - c) * (p - d))
    return area

# Пример значений для оснований и боковых сторон
a = float(input("длинна основания 1: "))  # длина первого основания
b =float(input("длинна основания 2: "))  # длина второго основания
c = float(input("длинна боковой стороны 1: "))  # длина первой боковой стороны
d = float(input("длинна боковой стороны 2:  ")) # длина второй боковой стороны

# Вычисляем площадь
area = trapecia_area(a, b, c, d)
print(f"Площадь трапеции: {area}")