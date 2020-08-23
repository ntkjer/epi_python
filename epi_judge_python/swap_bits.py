from test_framework import generic_test


def swap_bits(x, i, j):
    # Extract ith and jth bit, see if they're different
    if (x >> i) & 1 != (x >> j) & 1:
        # i and j are diff, lets swap
        # x ^ 1 = 0 when x = 1
        bit_mask = (1 << i) | (1 << j)
        x ^= bit_mask
    return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('swap_bits.py', 'swap_bits.tsv',
                                       swap_bits))