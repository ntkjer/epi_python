import collections
import functools

from typing import List

from test_framework import generic_test
from test_framework.test_failure import PropertyName

DuplicateAndMissing = collections.namedtuple('DuplicateAndMissing',
                                             ('duplicate', 'missing'))




def find_duplicate_missing(A: List[int]) -> DuplicateAndMissing:
    # compute XOR of all numbers from 0 to |A| - 1 and all entries in A
    miss_xor_dup = functools.reduce(lambda v, i: v ^ i[0] ^ i[1], enumerate(A), 0)

    # Find a bit thats set to 1 in miss_xor_dup
    # The bit must exist isf there is a single missing number and a single
    # duplicated number in A.

    # The bit-fiddling assignment below sets all of bits in differ_bit
    # to 0 except for the least significant bit in miss_xor_dup thats 1.
    differ_bit, miss_or_dup = miss_xor_dup & (~(miss_xor_dup - 1)), 0
    for i, a in enumerate(A):
        if i & differ_bit:
            miss_or_dup ^= i
        if a & differ_bit:
            miss_or_dup ^= a

    # miss_or_dup is either the missing val or the duplicated entry
    # if miss_or_dup is in A, miss_or_dup is the duplicated entry;
    # otherwise, miss_or_dup is the missing val.
    return (DuplicateAndMissing(miss_or_dup, miss_or_dup ^ miss_xor_dup) if miss_or_dup in A else
            DuplicateAndMissing(miss_or_dup ^ miss_xor_dup, miss_or_dup))


def res_printer(prop, value):
    def fmt(x):
        return 'duplicate: {}, missing: {}'.format(x[0], x[1]) if x else None

    return fmt(value) if prop in (PropertyName.EXPECTED,
                                  PropertyName.RESULT) else value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_for_missing_element.py',
                                       'find_missing_and_duplicate.tsv',
                                       find_duplicate_missing,
                                       res_printer=res_printer))
