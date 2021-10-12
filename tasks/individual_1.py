#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


def show_commands():
    """Список команд"""
    print("Список команд:\n")
    print("add - добавить студента;")
    print("list - вывести список студентов;")
    print("select - вывести список студентов, имеющих оценку 2;")
    print("exit - завершить работу с программой.")


def add_student():
    """Добавление студента"""
    # Запросить данные о студенте.
    name = input("Фамилия и инициалы? ")
    number = input("Номер группы? ")
    z = str(input('Успеваемость: '))
    # Создать словарь.
    student = {
        'name': name,
        'number': number,
        'z': z,
    }
    # Добавить словарь в список.
    students.append(student)
    # Отсортировать список в случае необходимости.
    if len(students) > 1:
        students.sort(key=lambda item: item.get('name', ''))


def show_list():
    """Вывод данных в таблицу"""
    # Заголовок таблицы.
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 20,
        '-' * 15
    )
    print(line)
    print(
        '| {:^4} | {:^30} | {:^20} | {:^15} |'.format(
            "№",
            "Ф.И.О.",
            "Группа",
            "Успеваемость"
        )
    )
    print(line)
    # Вывести данные о всех студентах.
    for idx, student in enumerate(students, 1):
        print(
            '| {:>4} | {:<30} | {:<20} | {:>15} |'.format(
                idx,
                student.get('name', ''),
                student.get('number', ''),
                student.get('z', 0)
            )
        )
    print(line)


def show_selected():
    """Проверка студентов, удовлетворяющих условию"""
    # Инициализировать счетчик.
    count = 0
    # Проверить сведения студентов из списка.
    for student in students:
        if "2" in student.get('z', ''):
            count += 1
            print(
                '{:>4} {}'.format('*', student.get('name', '')),
                '{:>1} {}'.format('группа №',
                                  student.get('number', ''))
            )
    if count == 0:
        print('Таких студентов нет')


def main():
    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            add_student()

        elif command == 'list':
            show_list()

        elif command.startswith('select'):
            show_selected()

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == '__main__':
    # Список студентов.
    students = []
    show_commands()

    main()
