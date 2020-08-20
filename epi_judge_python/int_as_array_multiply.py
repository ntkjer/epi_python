from typing import List

from test_framework import generic_test


def multiply(num1: List[int], num2: List[int]) -> List[int]:

    # [1, 4]
    # [1, 2]


    # 1.
    # [2, 8]
    # [1, 4]
    # [3, 12] or [4, 9]
    # [4, 2]

    # add last numbers
    # if over 9, save 9 as A[i]
    # append the sum, as if base 10 was not a boundary (e.g. 12)
    # [3, 9, 2]

    # [1, 2, 3]
    # [1, 8]

    # [ 8, 16, 24]
    # [ 1, 2 , 3]

    # [9, 18, 27]
    # reduce
    # [9 + 1, 9 + 2, 9, 7]
    # reduce
    # [10 + 1, 1 ,9 , 7]
    # reduce
    # [1, , 1, 9, 7]


    choice = num1
    if len(num1) <= len(num2):
        choice = num2

    return []


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_multiply.py',
                                       'int_as_array_multiply.tsv', multiply))
