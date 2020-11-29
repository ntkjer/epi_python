from test_framework import generic_test

import functools

@functools.lru_cache(None)
def compute_binomial_coefficient(n: int, k: int) -> int:
    if k in (0, n):
        return 1
    without_k = compute_binomial_coefficient(n - 1, k)
    with_k = compute_binomial_coefficient(n - 1, k - 1)
    return without_k + with_k


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('binomial_coefficients.py',
                                       'binomial_coefficients.tsv',
                                       compute_binomial_coefficient))
