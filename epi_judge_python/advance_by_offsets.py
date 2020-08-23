from typing import List

from test_framework import generic_test


def can_reach_end(A: List[int]) -> bool:
    last_index, reachable_moves = len(A) - 1, 0
    i = 0
    while i <= reachable_moves and reachable_moves < last_index:
        if i + A[i] > reachable_moves:
            reachable_moves = i + A[i]
        # reachable_moves = max(reachable_moves, A[i] + 1)
        i += 1

    return reachable_moves >= last_index


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end))
