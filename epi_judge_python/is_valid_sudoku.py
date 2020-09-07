from typing import List

from test_framework import generic_test

import math

# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku_2(partial_assignment: List[List[int]]) -> bool:

    def is_block_valid(block) -> bool:
        """
        Checks if there are duplicates and ignores 0
        """
        block = [i for i in block if i != 0]
        return len(set(block)) == len(block)

    def is_row_valid(partial_assignment: List[List]) -> bool:
        for row in partial_assignment:
            if not is_block_valid(row):
                return False
        return True

    def is_column_valid(partial_assignment: List[List]) -> bool:
        """
        unpack each list form partial_assignment
        and check if each moveset for that column is valid.
        """
        for column in zip(*partial_assignment):
            if not is_block_valid(column):
                return False
        return True

    def is_square_valid(partial_assignment: List[List]) -> bool:
        for i in range(0, 3, 6):
            for j in range(0, 3, 6):
                current_square = [partial_assignment[x][y]
                                  for x in range(i, i + 3)
                                  for y in range(j, j + 3)]
                if not is_block_valid(current_square):
                    return False
        return True

    if (not is_column_valid(partial_assignment)
        or not is_row_valid(partial_assignment)
        or is_square_valid(partial_assignment)):
        return False
    return True


def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:

    def has_duplicate(block):
        block = list(filter(lambda x: x != 0, block))
        return len(block) != len(set(block))

    n = len(partial_assignment)
    # check rows and columns
    if any(
        has_duplicate([partial_assignment[i][j] for j in range(n)])
        or has_duplicate([partial_assignment[j][i] for j in range(n)])
            for i in range(n)):
        return False

    region_size = int(math.sqrt(n))
    return all(not has_duplicate([
        partial_assignment[a][b]
        for a in range(region_size * h, region_size * (h + 1))
        for b in range(region_size * k, region_size * (k + 1))
    ]) for h in range(region_size) for k in range(region_size))



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_sudoku.py',
                                       'is_valid_sudoku.tsv', is_valid_sudoku))
