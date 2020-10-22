from typing import Iterator, List

from test_framework import generic_test

import heapq, itertools

def sort_approximately_sorted_array(sequence: Iterator[int],
                                    k: int) -> List[int]:
    min_heap: List[int] = []
    for x in itertools.islice(sequence, k):
        heapq.heappush(min_heap, x)
    result = []
    for x in sequence:
        # we will reach global min if we are at pos 3
        # keep extracting min and adding to result
        smallest = heapq.heappushpop(min_heap, x)
        result.append(smallest)
    while min_heap:
        result.append(heapq.heappop(min_heap))
    return result


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'sort_almost_sorted_array.py', 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
