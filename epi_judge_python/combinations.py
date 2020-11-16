from typing import List

from test_framework import generic_test, test_utils


def combinations(n: int, k: int) -> List[List[int]]:
    def generate_combinations(offset, partials):
        if len(partials) == offset:
            result.append(partials.copy())
        num_remaining = k - len(partials)
        i = offset
        while i <= n and num_remaining <= n - i + 1:
            generate_combinations(i + 1, partials + [i])
            i += 1

    result: List[List[int]] = []
    generate_combinations(1, [])
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'combinations.py',
            'combinations.tsv',
            combinations,
            comparator=test_utils.unordered_compare))
