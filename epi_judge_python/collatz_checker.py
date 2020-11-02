from test_framework import generic_test

from typing import Set

def test_collatz_conjecture(n: int) -> bool:
    # if odd, triple and add one
    # if even, halve it
    # we eventually arrive to 1
    # while n > 1:
    #     if n % 2 == 0:
    #         n = n // 2
    #     else:
    #         n = 3 * n + 1

    # store odd numbers already tested to converge to 1
    verified_numbers: Set[int] = set()

    for i in range(3, n + 1):
        sequence: Set[int] = set()
        test_i = i
        while test_i >= i:
            if test_i in sequence:
                # we've seen i, thus looping and failing conjecture
                # return false and short circuit
                return False
            sequence.add(test_i)
            if test_i % 2:
                if test_i in verified_numbers:
                    break
                verified_numbers.add(test_i)
                test_i = 3 * test_i + 1
            else:
                test_i //= 2
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('collatz_checker.py',
                                       'collatz_checker.tsv',
                                       test_collatz_conjecture))
