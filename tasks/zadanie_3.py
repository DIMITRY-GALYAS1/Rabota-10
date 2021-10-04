#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main():
    q = 1
    while True:
        z = int(input("Введите число: "))
        q *= z
        if q == 0:
            print("Произведение = 0")
            break
        else:
            print(f"Прозведение = {q}")


if __name__ == '__main__':
    main()
