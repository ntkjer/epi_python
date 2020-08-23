from typing import List

from test_framework import generic_test


# Given n, return all primes up to and including n.
def generate_primes_2(n: int) -> List[int]:
    """
    time to sift proportional to O(n/p)
    which is the series O(n/2 + n/3 + n/5 +...)

    a harmonic series that converges to O(n lg lg n)
    """
    if n < 2:
        return []

    primes = []
    is_prime = [False, False] + [True] * (n - 1)
    for p in range(2, n + 1):
        if is_prime[p]:
            primes.append(p)
            for i in range(p * 2, n + 1, p):
                is_prime[i] = False
    return primes


def generate_primes(n: int) -> List[int]:
    if n < 2:
        return []
    size = (n - 3) // 2 + 1
    primes = [2]

    #  Represents if 2i + 3 is prime or not for all i
    is_prime = [True] * size
    for i in range(size):
        if is_prime[i]:
            p = 2 * i + 3
            primes.append(p)

            #  Sieve from p^2
            #  p    = 2i + 3
            #  p^2  = 4i^2 + 12i + 9

            #  each item in is_prime represents 2i + 3
            #  so index = p^2/i = 4i^2 + 12i + 9 / 2i + 3

            #   --> 2i^2 + 6i + 3
            for j in range(2 * i**2 + 6 * i + 3, size, p):
                is_prime[j] = False

    return primes




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('prime_sieve.py', 'prime_sieve.tsv',
                                       generate_primes))
