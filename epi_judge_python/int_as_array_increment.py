from typing import List

from test_framework import generic_test


def plus_one_3(A: List[int]) -> List[int]:
    carry = True
    for i in reversed(range(len(A))):
        while carry:
            carry = False
            value, carry = increment(A[i])
            if i == 0 and (A[i] // 9 == 1):
                tmp = [1]
                A[i] = value
                A = tmp + A
                carry = False
            else:
                A[i] = value
                break
    return A


def plus_one(A: List[int]) -> List[int]:
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i - 1] += 1
    if A[0] == 10:
        A[0] = 1
        A.append(0)
    return A


def increment(x: int) -> (int, bool):
    result, carry = 0, False
    if x // 9 == 1:
        result, carry = 0, True
        return result, carry
    result = x + 1
    return result, carry


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
