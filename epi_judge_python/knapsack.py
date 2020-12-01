import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Item = collections.namedtuple('Item', ('weight', 'value'))

def optimum_subject_to_capacity_iter(items: List[Item], capacity: int) -> int:
    dp = [[0 for _ in range(capacity + 1)] for _ in range(len(items))]
    return

def optimum_subject_to_capacity(items: List[Item], capacity: int) -> int:
    # DP[i, j] = max(DP[i + 1,
    #                vi + DP[i + 1, j − Si])
    # dp = [[0 for item in range(len(items) + 1)]
    #       for cap in range(capacity + 1)]
    @functools.lru_cache(None)
    def optimum_subject_to_item_and_cap(k, available_capacity):
        if k < 0:
            return 0
        without_curr_item = optimum_subject_to_item_and_cap(k - 1, available_capacity)
        curr_weight = items[k].weight
        if available_capacity < curr_weight:
            with_curr_item = 0
        else:
            with_curr_item = items[k].value + optimum_subject_to_item_and_cap(k - 1,
                                                                              available_capacity - curr_weight)
        return max(with_curr_item, without_curr_item)

    return optimum_subject_to_item_and_cap(len(items) - 1, capacity)


@enable_executor_hook
def optimum_subject_to_capacity_wrapper(executor, items, capacity):
    items = [Item(*i) for i in items]
    return executor.run(
        functools.partial(optimum_subject_to_capacity, items, capacity))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('knapsack.py', 'knapsack.tsv',
                                       optimum_subject_to_capacity_wrapper))
