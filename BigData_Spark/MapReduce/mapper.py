#!/usr/bin/env python


def mapper(file):
    """
    Mapper mapping to 2D Matrix
    :param file:
    :return: mapped 2D matrix
    """
    file = open(file)
    matrix = []
    for line in file:
        rows = []
        for word in line.split():
            rows.append((word.strip(',').strip('"'), 1))
        matrix.append(rows)
    return matrix
