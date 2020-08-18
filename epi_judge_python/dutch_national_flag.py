import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


def dutch_flag_partition_slow(pivot_index: int, A: List[int]) -> None:
    pivot_val = A[pivot_index]
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if A[j] < pivot_val:
                A[j], A[i] = A[i], A[j]
                break
    for i in reversed(range(len(A))):
        for j in reversed(range(i)):
            if A[j] > pivot_val:
                A[i], A[j] = A[j], A[i]
                break


def dutch_flag_partition_2(pivot_index: int, A: List[int]) -> None:
    pivot = A[pivot_index]
    smaller, equal, larger = 0, 0, len(A)
    while equal < larger:
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller, equal = smaller + 1, equal + 1
        elif A[equal] == pivot:
            equal += 1
        else:
            larger -= 1
            A[equal], A[larger] = A[larger], A[equal]


def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    lt, i, gt = 0, 0, len(A)
    pivot = A[pivot_index]
    while i < gt:
        if A[i] < pivot:
            A[lt], A[i] = A[i], A[lt]
            i, lt = i + 1, lt + 1
        elif A[i] > pivot:
            gt -= 1
            A[i], A[gt] = A[gt], A[i]
        else:
            i += 1


@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure('Some elements are missing from original array')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('dutch_national_flag.py',
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
