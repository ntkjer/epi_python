from test_framework import generic_test

import swap_bits


def generate_reversed_table() -> list:
    result = []
    for i in range(2**16 - 1):
        tmp = i
        for j in range(8):
            tmp = swap_bits.swap_bits(tmp, j, 15-j)
        result.append(tmp)
    return result


def reverse_bits(x: int) -> int:
    """
    We divide x, a 64-bit number at most, into four 16-bit partitions.
    x = ABCD which the rev(x) = rev(D)rev(C)rev(B)rev(A)

        Results are bit shifted by mask_size
    to move the bits we care about in the right position.

        We also apply a mask_size of 16 to only preserve the
    bits needed for each quadrant.

    E.g
        A = x & bit_mask
    because we only need the first 16 bits of that bit sequence

        B is shifted by 16 before the masking because
    we care about the second 16bit sequence in x, so quad-2

        C is twice that for quadrant 3.

        D is shifted thrice before masking
    as we've already looked at the first 48 bits.

        When we return x we shift each answer to reverse the order
    of each bit before looking them up in the table.

        So to get rev(x) when x is 64 bit binary int
        and x is ABCD, s.t. each partition is 16bits:

        x = A|B|C|D, rev(x) = rev[D] | rev[C] | rev[B] | rev[A]
    which is why we shift the appropriate bits in their respective quadrants.

    """
    mask_size = 16
    bit_mask = 0xFFFF
    reversed = _REVERSED_VALUES
    A = x & bit_mask
    B = x >> mask_size & bit_mask
    C = x >> (2 * mask_size) & bit_mask
    D = x >> (3 * mask_size) & bit_mask
    return (reversed[A] << (3 * mask_size) |
            reversed[B] << (2 * mask_size) |
            reversed[C] << (mask_size) |
            reversed[D])


def reverse_bits_brute_force(x: int) -> int:
    """
    needs padding for trailing bits
    """
    i, j = 1, x.bit_length() + 1
    while j > x.bit_length() / 2:
        if (x >> i) & 1 != (x >> j) & 1:
            bit_mask = (1 << i) | (1 << j)
            x ^= bit_mask
        i += 1
        j -= 1
    return x


if __name__ == '__main__':
    _REVERSED_VALUES = generate_reversed_table()

    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
