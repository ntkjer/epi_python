from typing import Iterator

from test_framework import generic_test
from test_framework.test_failure import TestFailure

import itertools

def find_missing_element(stream: Iterator[int]) -> int:
    num_bucket = 1 << 16  # 2ˆ16 - 1
    counter = [0] * num_bucket
    stream, stream_copy = itertools.tee(stream)

    for x in stream:
        upper_part_x = x >> 16
        counter[upper_part_x] += 1

    # look for a bucket hat contains less than (1 << 16) elems
    bucket_cap = 1 << 16
    candidate_bucket = next(i for i, c in enumerate(counter) if c < bucket_cap)

    # Finds all IP adcdresses in stream whose first 16 bits are equal to candidate
    candidates = [0] * bucket_cap
    for x in stream_copy:
        upper_part_x = x >> 16
        if candidate_bucket == upper_part_x:
            # records the 16 lsb of x
            lower_part_x = ((1 << 16) - 1) & x
            candidates[lower_part_x] = 1

    # at least one lsb combination is absent, we find it
    for i, v in enumerate(candidates):
        if v == 0:
            return (candidate_bucket << 16) | i


def find_missing_element_wrapper(stream):
    try:
        res = find_missing_element(iter(stream))
        if res in stream:
            raise TestFailure('{} appears in stream'.format(res))
    except ValueError:
        raise TestFailure('Unexpected no missing element exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('absent_value_array.py',
                                       'absent_value_array.tsv',
                                       find_missing_element_wrapper))
