from test_framework import generic_test
from test_framework.test_failure import TestFailure

import functools
import string


def int_to_string(x: int) -> str:
    negative = False
    if x < 0:
        x, negative = -x, True
    result = []

    while x:
        result.append(chr(ord('0') + x % 10))
        x //= 10
        if x == 0:
            break

    return ('-' if negative else '') + ''.join(reversed(result))


def string_to_int_2(s: str) -> int:
    return (-1 if s[0] == "-" else 1) * functools.reduce(
        lambda running_sum, c: running_sum * 10 + string.digits.index(c),
        s[s[0] in '+-':], 0)


def string_to_int(s: str) -> int:
    sign, start, result = 1, 0, 0
    if s[0] == "-":
        sign *= -1
        start += 1
    elif s[0] == "+":
        start += 1
    for i in range(start, len(s)):
        result = result * 10
        result += string.digits.index(s[i])
    return sign * result


def string_to_int_3(s: str) -> int:
    sign = 1
    start = 0

    if s[0] == "+":
        start += 1
    elif s[0] == "-":
        start += 1
        sign *= -1
    result = 0

    for i in range(start, len(s)):
        result = result * 10
        result += ord(s[i]) - 48

    return sign * result


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
