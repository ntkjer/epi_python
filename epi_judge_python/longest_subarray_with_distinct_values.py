from typing import List, Dict

from test_framework import generic_test

import collections

def longest_subarray_with_distinct_entries(A: List[int]) -> int:
    most_recent_occurence: Dict[int, int] = {}
    longest_dup_free_subarr_start_idx = result = 0
    for i, a in enumerate(A):
        # Defer updating dup_idx until we see dup
        if a in most_recent_occurence:
            dup_idx = most_recent_occurence[a]
            # A[i] appeared before
            # Did it appear in longest current subarr?
            if dup_idx >= longest_dup_free_subarr_start_idx:
                result = max(result, i - longest_dup_free_subarr_start_idx)
                longest_dup_free_subarr_start_idx = dup_idx + 1
        most_recent_occurence[a] = i
    return max(result, len(A) - longest_dup_free_subarr_start_idx)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'longest_subarray_with_distinct_values.py',
            'longest_subarray_with_distinct_values.tsv',
            longest_subarray_with_distinct_entries))
