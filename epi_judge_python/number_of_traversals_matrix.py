from test_framework import generic_test

import functools

def number_of_ways(n: int, m: int) -> int:
    lookup = [[1 for _ in range(n)] for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            lookup[i][j] = lookup[i - 1][j] + lookup[i][j - 1]

    return lookup[-1][-1]

def number_of_ways(n: int, m: int) -> int:
    @functools.lru_cache(None)
    def compute_number_of_ways_to_xy(x, y):
        if x == y == 0:
            return 1
        ways_top = 0 if x == 0 else compute_number_of_ways_to_xy(x - 1, y)
        ways_left = 0 if y == 0 else compute_number_of_ways_to_xy(x, y - 1)
        return ways_left + ways_top
    return compute_number_of_ways_to_xy(n - 1, m - 1)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_traversals_matrix.py',
                                       'number_of_traversals_matrix.tsv',
                                       number_of_ways))
