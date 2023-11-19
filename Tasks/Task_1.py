#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    value1 = input("Введите первое значение: ")
    value2 = input("Введите второе значение: ")

    try:
        value1 = float(value1)
        value2 = float(value2)
        result = value1 + value2
    except ValueError:
        result = str(value1) + str(value2)

    print("Результат: ", result)
