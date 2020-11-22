from test_framework import generic_test

import functools

def levenshtein_distance(A: str, B: str) -> int:
    # S A T U R D A Y
    # S U N D A Y
    # >> 4

    # S  T U R D A Y
    # S    U R D A Y
    # S    U N D A Y
    #    S U N D A Y
    # S U N D A Y

    # A C
    # A B

    # if  l_d = E(A[0, a - 1], B[0, b -  1]), same last char
    # then l_d = E(A[0, a - 2], B[0, b - 2]), diff last char
    @functools.lru_cache(None)
    def compute_distance_between_prefixes(A_idx, B_idx):
        if A_idx < 0:
            # A is empty so add all of B's characters
            return B_idx + 1
        elif B_idx < 0:
            # B is empty so delete all of A's chars
            return A_idx + 1
        if A[A_idx] == B[B_idx]:
            return compute_distance_between_prefixes(A_idx - 1, B_idx - 1)

        subsitute_last = compute_distance_between_prefixes(A_idx - 1, B_idx - 1)
        add_last = compute_distance_between_prefixes(A_idx, B_idx - 1)
        delete_last = compute_distance_between_prefixes(A_idx - 1, B_idx)
        return 1 + min(subsitute_last, add_last, delete_last)

    return compute_distance_between_prefixes(len(A) - 1, len(B) - 1)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('levenshtein_distance.py',
                                       'levenshtein_distance.tsv',
                                       levenshtein_distance))
