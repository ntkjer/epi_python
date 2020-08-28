import functools
from typing import List, Dict

from test_framework import generic_test
from test_framework.random_sequence_checker import (
    binomial_coefficient, check_sequence_is_uniformly_random,
    compute_combination_idx, run_func_with_retries)
from test_framework.test_utils import enable_executor_hook

import random


def random_subset_2(n: int, k: int) -> List[int]:
    """
    book solution
    """
    modified_elems: Dict[int, int] = {}
    for i in range(k):
        random_idx = random.randrange(i, n)  # generate [1, n-1]
        random_val = modified_elems.get(random_idx, random_idx)
        curr_val = modified_elems.get(i, i)
        modified_elems[random_idx] = curr_val
        modified_elems[i] = random_val
    return [modified_elems[i] for i in range(k)]


def random_subset(n: int, k: int) -> List[int]:
    result = {}
    for i in range(k):
        r_idx = random.randrange(i, n)
        r_val = result.get(r_idx, r_idx)
        i_val = result.get(i, i)
        result[r_idx] = i_val
        result[i] = r_val
    return [result[i] for i in range(k)]


@enable_executor_hook
def random_subset_wrapper(executor, n, k):
    def random_subset_runner(executor, n, k):
        results = executor.run(
            lambda: [random_subset(n, k) for _ in range(100000)])

        total_possible_outcomes = binomial_coefficient(n, k)
        comb_to_idx = {
            tuple(compute_combination_idx(list(range(n)), n, k, i)): i
            for i in range(binomial_coefficient(n, k))
        }
        return check_sequence_is_uniformly_random(
            [comb_to_idx.get(tuple(sorted(result)), 0) for result in results],
            total_possible_outcomes, 0.01)

    run_func_with_retries(
        functools.partial(random_subset_runner, executor, n, k))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('random_subset.py', 'random_subset.tsv',
                                       random_subset_wrapper))
