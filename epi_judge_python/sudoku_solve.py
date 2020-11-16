import copy
import functools
import math
import itertools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def solve_sudoku(partial_assignment: List[List[int]]) -> bool:
    def find_unassigned():
        for row in range(9):
            for col in range(9):
                if partial_assignment[row][col] == 0:
                    return row, col
        return -1, -1

    def safe_to_place(row, col, val) -> bool:
        box_row = row - row % 3
        box_col = col - col % 3
        if check_col(col, val) and check_row(row, val) and check_square(box_row, box_col, val):
            return True
        return False

    def check_col(col, val):
        for row in range(9):
            if partial_assignment[row][col] == val:
                return False
        return True

    def check_row(row, val):
        for col in range(9):
            if partial_assignment[row][col] == val:
                return False
        return True

    def check_square(row, col, val):
        for r in range(row, row + 3):
            for c in range(col, col + 3):
                if partial_assignment[r][c] == val:
                    return False
        return True

    def solved():
        row, col = find_unassigned()
        if row is -1 and col is -1:
            return True

        candidates = [i for i in range(1, 10)]
        for candidate in candidates:
            if safe_to_place(row, col, candidate):
                partial_assignment[row][col] = candidate
                if solved():
                    return True
                partial_assignment[row][col] = 0
        return False

    return solved()

def assert_unique_seq(seq):
    seen = set()
    for x in seq:
        if x == 0:
            raise TestFailure('Cell left uninitialized')
        if x < 0 or x > len(seq):
            raise TestFailure('Cell value out of range')
        if x in seen:
            raise TestFailure('Duplicate value in section')
        seen.add(x)


def gather_square_block(data, block_size, n):
    block_x = (n % block_size) * block_size
    block_y = (n // block_size) * block_size

    return [
        data[block_x + i][block_y + j] for j in range(block_size)
        for i in range(block_size)
    ]


@enable_executor_hook
def solve_sudoku_wrapper(executor, partial_assignment):
    solved = copy.deepcopy(partial_assignment)

    executor.run(functools.partial(solve_sudoku, solved))

    if len(partial_assignment) != len(solved):
        raise TestFailure('Initial cell assignment has been changed')

    for (br, sr) in zip(partial_assignment, solved):
        if len(br) != len(sr):
            raise TestFailure('Initial cell assignment has been changed')
        for (bcell, scell) in zip(br, sr):
            if bcell != 0 and bcell != scell:
                raise TestFailure('Initial cell assignment has been changed')

    block_size = int(math.sqrt(len(solved)))
    for i, solved_row in enumerate(solved):
        assert_unique_seq(solved_row)
        assert_unique_seq([row[i] for row in solved])
        assert_unique_seq(gather_square_block(solved, block_size, i))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sudoku_solve.py', 'sudoku_solve.tsv',
                                       solve_sudoku_wrapper))
