from test_framework import generic_test

import functools
import time

def levenshtein_distance(A: str, B: str) -> int:
    # S A T U R D A Y
    # S U N D A Y
    # >> 4

    # if  l_d = E(A[0, a - 1], B[0, b -  1]), same last char
    # then l_d = E(A[0, a - 2], B[0, b - 2]), diff last char
    # in general we take the min of the current levenshetin dist + 1 out of three cases

    # bottom-up
    lookup = [[0 for i in range(len(B) + 1)] for j in range(len(A) + 1)]
    for i in range(len(A) + 1):
        lookup[i][0] = i

    for i in range(len(B) + 1):
        lookup[0][i] = i

    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            if A[i - 1] == B[j - 1]:
                lookup[i][j] = lookup[i - 1][j - 1]
            else:
                add_last = 1 + lookup[i][j - 1]
                delete_last = 1 + lookup[i - 1][j]
                sub_last = 1 + lookup[i - 1][j - 1]
                lookup[i][j] = min(add_last, delete_last, sub_last)
    return lookup[-1][-1]

















#     # top-down solution from book
#     @functools.lru_cache(None)
#     def compute_distance_between_prefixes(A_idx, B_idx):
#         if A_idx < 0:
#             # A is empty so add all of B's characters
#             return B_idx + 1
#         elif B_idx < 0:
#             # B is empty so delete all of A's chars
#             return A_idx + 1
#         if A[A_idx] == B[B_idx]:
#             return compute_distance_between_prefixes(A_idx - 1, B_idx - 1)
#
#         substitute_last = compute_distance_between_prefixes(A_idx - 1, B_idx - 1)
#         add_last = compute_distance_between_prefixes(A_idx, B_idx - 1)
#         delete_last = compute_distance_between_prefixes(A_idx - 1, B_idx)
#         return 1 + min(substitute_last, add_last, delete_last)
#
#     return compute_distance_between_prefixes(len(A) - 1, len(B) - 1)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('levenshtein_distance.py',
                                       'levenshtein_distance.tsv',
                                       levenshtein_distance))
