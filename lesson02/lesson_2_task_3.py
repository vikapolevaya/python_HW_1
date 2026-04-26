import math


def square(side):
    return math.ceil(side * side)


side = float(input("Введите сторону квадрата: "))
area = square(side)

print("Площадь квадрата:", area)
