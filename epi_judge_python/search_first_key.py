from typing import List

from test_framework import generic_test


def search_first_of_k(A: List[int], k: int) -> int:
    lo, hi, result = 0, len(A) - 1, -1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if k == A[mid]:
            result = mid
            hi = mid - 1
        elif A[mid] < k:
            lo = mid + 1
        else:
            hi = mid - 1
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
