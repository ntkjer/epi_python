from typing import List

from test_framework import generic_test

import time

def minimum_path_weight_book(triangle: List[List[int]]) -> int:
    min_weight_to_curr_row = [0]
    for row in triangle:
        min_weight_to_curr_row = [
            row[j] + min(
                min_weight_to_curr_row[max(j - 1, 0)],
                min_weight_to_curr_row[min(j, len(min_weight_to_curr_row) - 1)])
            for j in range(len(row))
        ]
    return min(min_weight_to_curr_row)

def minimum_path_weight(triangle: List[List[int]]) -> int:
    if not triangle:
        return 0

    memo = {}

    def recur_min_path(i, j):
        if (i, j) in memo:
            return memo[i, j]

        if j == len(triangle):
            return 0
        curr_min_weight = triangle[j][i] + min(recur_min_path(i, j + 1), recur_min_path(i + 1, j + 1))
        memo[i, j] = curr_min_weight
        return memo[i, j]

    return recur_min_path(0, 0)


def minimum_path_weight_iter(triangle: List[List[int]]) -> int:
    if not triangle:
        return 0

    res = [[0 for i in range(len(row))] for row in triangle]
    res[0][0] = triangle[0][0]
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                # left adj
                res[i][j] = res[i - 1][j] + triangle[i][j]
            elif j == len(triangle[i]) - 1:
                # right  adj
                res[i][j] = res[i - 1][j - 1] + triangle[i][j]
            else:
                res[i][j] = min(res[i - 1][j - 1], res[i - 1][j]) + triangle[i][j]
    return min(res[-1])

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'minimum_weight_path_in_a_triangle.py',
            'minimum_weight_path_in_a_triangle.tsv', minimum_path_weight))
