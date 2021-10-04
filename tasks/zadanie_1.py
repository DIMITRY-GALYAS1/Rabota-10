#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def test():
    z = int(input('Введите число:'))
    if z > 0:
        positive(z)
    else:
        negative(z)


def positive(z):
    print(f"{z} положительное")


def negative(z):
    print(f"{z} отрицательное")


if __name__ == '__main__':
    test()
