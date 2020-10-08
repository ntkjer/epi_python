from typing import Iterator, List

from test_framework import generic_test

import collections


def examine_buildings_with_sunset(sequence: Iterator[int]) -> List[int]:
    # process buildings from east to west
    candidates = []
    for building_idx, building_height in enumerate(sequence):
        while candidates and building_height >= candidates[-1][-1]:
            candidates.pop()
        candidates.append((building_idx, building_height))

    # return in west-to east order
    return [c[0] for c in reversed(candidates)]


def examine_buildings_with_sunset_2(sequence: Iterator[int]) -> List[int]:
    BuildingWithHeight = collections.namedtuple('BuildingWithHeight',
                                                ('id', 'height'))
    candidates: List[BuildingWithHeight] = []
    for building_idx, building_height in enumerate(sequence):
        while candidates and building_height >= candidates[-1].height:
            candidates.pop()
        candidates.append(BuildingWithHeight(building_idx, building_height))
    return [c.id for c in reversed(candidates)]


def examine_buildings_with_sunset_wrapper(sequence):
    return examine_buildings_with_sunset(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sunset_view.py', 'sunset_view.tsv',
                                       examine_buildings_with_sunset))
