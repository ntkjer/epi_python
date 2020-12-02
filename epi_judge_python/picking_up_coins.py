from typing import List

from test_framework import generic_test

import functools

def maximum_revenue(coins: List[int]) -> int:
    @functools.lru_cache(None)
    def compute_max_revenue_for_range(a, b):
        if a > b:
            # no coins left
            return 0
        max_revenue_a = coins[a] + min(
            compute_max_revenue_for_range(a + 2, b),
            compute_max_revenue_for_range(a + 1, b - 1))
        max_revenue_b = coins[b] + min(
            compute_max_revenue_for_range(a + 1, b - 1),
            compute_max_revenue_for_range(a, b - 2))
        return max(max_revenue_a, max_revenue_b)

    return compute_max_revenue_for_range(0, len(coins) - 1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('picking_up_coins.py',
                                       'picking_up_coins.tsv',
                                       maximum_revenue))
