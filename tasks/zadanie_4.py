#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def get_input():
    z = input('Введите строку: ')
    test_input(z)


def test_input(z):
    try:
        str_to_int(z)
    except ValueError:
        print('Нельзя преобразовать в число')


def str_to_int(z):
    i = int(z)
    print_int(i)


def print_int(i):
    print(i)


if __name__ == '__main__':
    get_input()
