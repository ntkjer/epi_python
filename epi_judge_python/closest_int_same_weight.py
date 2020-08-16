from test_framework import generic_test

import sys


def closest_int_same_bit_count_not_optimal(x: int) -> int:
    num_unsigned_bits = 64
    for i in range(num_unsigned_bits - 1):
        if (x >> i) & 1 != (x >> (i + 1)) & 1:
            x ^= (1 << i) | (1 << (i + 1))
            return x

    raise ValueError("All bits are 0 or 1")


def closest_int_same_bit_count(x: int) -> int:
    # IF all bits are either all 0 or 1, there cant be an answer.
    if x & sys.maxsize in {sys.maxsize, 0}:
        raise ValueError("All bits are 1 or 0")

    rightmost_bit = x & ~(x - 1)
    next_unset_bit = ~x & (x + 1)

    if next_unset_bit > rightmost_bit:
        # 0 shifted to the right 0111 -> 1011
        x ^= next_unset_bit | next_unset_bit >> 1
    else:
        # 1 shifted to the right 1000 -> 0100
        x ^= rightmost_bit | rightmost_bit >> 1
    return x


def closest_int_same_bit_count_optimal(x: int) -> int:
    if ((x & 1) == 0):
        # LSB = 0
        # x = 10001000
        first_one = x & ~(x - 1)  # Get first one, 01000
        x = x & (x - 1)
        # x = 1000000
        x = x | (first_one >> 1)
        # x = 10000100
    else:
        first_zero = ~x & ~(~x - 1)
        x = x & ~(1)
        x = x | first_zero
    return x


def closest_int_same_bit_count_first_try(x: int) -> int:
    """
    when x is 3, y is is 5, d is 2
    when x is 2, y is 1, d is 1
    when x is 1, y is 2, d is 1

    We look to right if its possible to right shift the LSB
    else we shift left hte MSB.

    """
    lsb = x & ~(x - 1)
    lsb = lsb >> 1
    result = x & (x - 1)
    result = result | lsb

    if result > x:
        print("result greater than x, get hi")
        msb = 1
        tmp = x
        while tmp:
            tmp >>= 1
            msb <<= 1
        x = x & ~msb
        msb <<= 1
        result = x | msb
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('closest_int_same_weight.py',
                                       'closest_int_same_weight.tsv',
                                       closest_int_same_bit_count))
