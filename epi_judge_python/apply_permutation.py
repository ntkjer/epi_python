from typing import List

from test_framework import generic_test

import time
def apply_permutation_bf(perm: List[int], A: List[int]) -> None:
    assert(len(perm) == len(A))
    result = [0] * len(A)
    for i in range(len(A)):
        #  print(i, perm[i])
        result[perm[i]] = A[i]
    A = result
    return


def apply_permutation(perm: List[int], A: List[int]) -> None:
    print("testing..")
    print(A)
    print(perm)
    for i in range(len(A)):
        print("i: ", i, ", perm[i]:", perm[i], ", A[i]: ", A[i])
        while perm[i] != i:
            print("A[perm[i]]: ", A[perm[i]], ", A[i]:", A[i])
            A[perm[i]], A[i] = A[i], A[perm[i]]
            print("perm[perm[i]]: ", perm[perm[i]], ", perm[i]: ", perm[i])
            perm[perm[i]], perm[i] = perm[i], perm[perm[i]]
    print(A)
    time.sleep(5)


def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('apply_permutation.py',
                                       'apply_permutation.tsv',
                                       apply_permutation_wrapper))
