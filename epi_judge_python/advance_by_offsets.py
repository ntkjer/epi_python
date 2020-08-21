from typing import List

from test_framework import generic_test


def can_reach_end(A: List[int]) -> bool:
    solved = len(A) - 1
    max_moves = 0
    i = 0
    while i <= max_moves and max_moves < solved:
        if i + A[i] > max_moves:
            max_moves = i + A[i]
            # max_moves = max(max_moves, A[i] + 1)
        i += 1
    return max_moves >= solved


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end))
