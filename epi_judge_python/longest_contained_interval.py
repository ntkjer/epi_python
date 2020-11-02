from typing import List

from test_framework import generic_test


def longest_contained_range(A: List[int]) -> int:
    entries = set(A)
    max_interval = 0
    while entries:
        curr_entry = entries.pop()
        left = curr_entry - 1
        right = curr_entry + 1
        while left in entries:
            entries.remove(left)
            left -= 1
        while right in entries:
            entries.remove(right)
            right += 1
        # right - left - 1 b.c sentinels are overshot by +1,-1 for r,l
        # so for longest subsequence of k, we get k + 1
        # subtract another 1 off
        max_interval = max(max_interval, right - left - 1)
    return max_interval


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('longest_contained_interval.py',
                                       'longest_contained_interval.tsv',
                                       longest_contained_range))
