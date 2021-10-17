#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def cylinder():
    def circle():
        return math.pi * radius ** 2

    height = float(input("Введите высоту: "))
    radius = float(input("Введите радиус: "))
    z = input("1 - Площадь боковой поверхности, "
              "2 - Полная площадь цилиндра: ")
    side = 2 * math.pi * radius * height

    if z == "1":
        print("Площадь боковой поверхности:", side)
    elif z == "2":
        st_circle = circle()
        full_pl = side + 2 * st_circle
        print("Полная площадь:", full_pl)
    else:
        print("Неизвестная команда")


if __name__ == '__main__':
    cylinder()
