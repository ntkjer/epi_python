from typing import List

from test_framework import generic_test

import math

def search_smallest(A: List[int]) -> int:
    lo, hi = 0, len(A) - 1
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if A[mid] > A[hi]:
            # min must be in A[mid + 1:hi + 1]
            lo = mid + 1
        else:
            # min cant be in A[mid + 1:hi + 1]
            # it must be in A[lo: mid + 1]
            hi = mid
    return lo


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_shifted_sorted_array.py',
                                       'search_shifted_sorted_array.tsv',
                                       search_smallest))
