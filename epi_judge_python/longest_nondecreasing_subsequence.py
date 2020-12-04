from typing import List

from test_framework import generic_test


def book_longest_nondecreasing_subsequence_length(A: List[int]) -> int:
    # [4, 0, 3, 3, 7, 5, 7]
    # len: 3
    max_length = [1] * len(A)
    for i in range(1, len(A)):
        max_length[i] = 1 + max(
            (max_length[j] for j in range(i) if A[i] >= A[j]), default=0)
    return max(max_length)

def longest_nondecreasing_subsequence_length(A: List[int]) -> int:
    """Tn = O(nlgn)
    Still uses n space
    """
    def binary_search(sub, val):
        lo, hi = 0, len(sub)
        while lo < hi:
            mid = (lo + hi) // 2
            if val > sub[mid]:
                lo = mid + 1
            elif val < sub[mid]:
                hi = mid - 1
            else:
                return mid
        return lo

    sub = []
    for val in A:
        i, sub_len = binary_search(sub, val), len(sub)
        while i <= sub_len:
            if i == sub_len:
                sub.append(val)
                break
            elif val < sub[i]:
                sub[i] = val
                break
            else:
                i += 1
    return len(sub)

def nlgn_longest_nondecreasing_subsequence_length(A: List[int]) -> int:
    tails = [1] * len(A)
    size = 0
    for x in A:
        i, j = 0, size
        while i != j:
            m = (i + j) // 2
            if tails[m] < x:
                i = m + 1
            else:
                j = m
        tails[i] = x
        size = max(i + 1, size)

    return size



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'longest_nondecreasing_subsequence.py',
            'longest_nondecreasing_subsequence.tsv',
            longest_nondecreasing_subsequence_length))
