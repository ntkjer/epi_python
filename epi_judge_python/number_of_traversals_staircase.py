from test_framework import generic_test


def number_of_ways_to_top(top: int, maximum_step: int) -> int:
    def compute_num_ways_to_h(h):
        if h <= 1:
            return 1

        return sum(compute_num_ways_to_h(h - i)
                   for i in range(1, min(maximum_step, h) + 1))

    return compute_num_ways_to_h(top)




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_traversals_staircase.py',
                                       'number_of_traversals_staircase.tsv',
                                       number_of_ways_to_top))
