from typing import List

from test_framework import generic_test


def generate_pascal_triangle(n: int) -> List[List[int]]:
    # result = [[1] * (i + 1) for i in range(n)]
    result = []
    for i in range(n):
        result.append([1] * (i + 1))

    for i in range(len(result)):
        for j in range(1, i):
            result[i][j] = result[i - 1][j - 1] + result[i - 1][j]

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('pascal_triangle.py',
                                       'pascal_triangle.tsv',
                                       generate_pascal_triangle))
