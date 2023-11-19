#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import MyExceptions as me


def generate_matrix(rows, columns, range_start, range_end):
    matrix = []
    for _ in range(rows):
        row = []
        for _ in range(columns):
            row.append(random.randint(range_start, range_end))
        matrix.append(row)
    return matrix


if __name__ == "__main__":
    while True:
        try:
            rows = int(input("Введите количество строк: "))
            columns = int(input("Введите количество столбцов: "))
            range_start = int(input("Введите начало диапазона целых чисел: "))
            range_end = int(input("Введите конец диапазона целых чисел: "))

            if rows <= 0 or columns <= 0 or range_start > range_end:
                raise me.InvalidRangeValueException("Неверный диапазон!")
            break
        except me.InvalidRangeValueException as e:
            print(str(e))

    matrix = generate_matrix(rows, columns, range_start, range_end)
    print("Сгенерированная матрица:")
    for row in matrix:
        print(row)
