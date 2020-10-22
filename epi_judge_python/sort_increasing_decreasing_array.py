from typing import List

from test_framework import generic_test

import heapq

def sort_k_increasing_decreasing_array(A: List[int]) -> List[int]:
    # split A into dec or inc sublists
    sorted_subarr = []
    increasing, decreasing = range(2)
    subarr_type = increasing
    start_idx = 0
    for i in range(1, len(A) + 1):
        if (i == len(A) or
            (A[i - 1] < A[i] and subarr_type is decreasing) or
            (A[i - 1] >= A[i] and subarr_type is increasing)):
            sorted_subarr.append(A[start_idx:i] if subarr_type ==
                                    increasing else A[i - 1:start_idx - 1: -1])
            start_idx = i
            subarr_type = (decreasing if subarr_type is increasing else increasing)
    return list(heapq.merge(*sorted_subarr))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sort_increasing_decreasing_array.py',
                                       'sort_increasing_decreasing_array.tsv',
                                       sort_k_increasing_decreasing_array))
