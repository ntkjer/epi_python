from typing import List

from test_framework import generic_test, test_utils


def permutations(A: List[int]) -> List[List[int]]:
    def permute(idx):
        if idx == len(A) - 1:
            result.append(A.copy())
            return

        for j in range(idx, len(A)):
            A[idx], A[j] = A[j], A[idx]
            permute(idx + 1)
            A[idx], A[j] = A[j], A[idx]

    result: List[List[int]] = []
    permute(0)
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('permutations.py', 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))
