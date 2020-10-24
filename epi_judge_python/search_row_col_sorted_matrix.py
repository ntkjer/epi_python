from typing import List

from test_framework import generic_test


def matrix_search(A: List[List[int]], x: int) -> bool:
    """
    Each iteration either removes a row or column
    leading to m + n - 1 compares.
    O(m + n) time complexity
    """
    # start at top right col
    row, col = 0, len(A[0]) - 1
    while row < len(A) and col >= 0:
        if A[row][col] == x:
            return True
        elif A[row][col] < x:
            # eliminate this row
            row += 1
        else:
            # A[row][col] > x
            # eliminate this col
            col -= 1
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_row_col_sorted_matrix.py',
                                       'search_row_col_sorted_matrix.tsv',
                                       matrix_search))
