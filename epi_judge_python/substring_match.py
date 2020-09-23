from test_framework import generic_test

import functools


def rabin_karp(t: str, s: str) -> int:
    if len(s) > len(t):
        return -1

    base = 26
    # Generate hash codes for s and t
    t_hash = functools.reduce(lambda h, c: h * base + ord(c), t[:len(s)], 0)
    s_hash = functools.reduce(lambda h, c: h * base + ord(c), s, 0)
    power_s = base**max(len(s) - 1, 0)  # base^[s-1]

    for i in range(len(s), len(t)):
        if t_hash == s_hash and t[i - len(s):i] == s:
            return i - len(s)  # match

        # Rolling hash to compute hash code
        t_hash -= ord(t[i - len(s)]) * power_s
        t_hash = t_hash * base + ord(t[i])

    if t_hash == s_hash and t[-len(s):] == s:
        return len(t) - len(s)

    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('substring_match.py',
                                       'substring_match.tsv', rabin_karp))
