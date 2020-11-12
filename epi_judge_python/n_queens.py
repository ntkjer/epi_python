from typing import List

from test_framework import generic_test


def n_queens(n: int) -> List[List[int]]:
    def nQueens(size):
        board = [-1] * size
        rQueens(board, 0, size)
        print(board)

    # This procedure checks that the most recently placed queen on column current
    # does not conflict with queens in columns to the left.
    def noConflicts(board, current):
        for i in range(current):
            if (board[i] == board[current]):
                return False
            if (current - i == abs(board[current] - board[i])):
                return False
        return True

        # This procedure places a queens on the board on a given column so it does

    # not conflict with the existing queens, and then calls itself recursively
    # to place subsequent queens till the requisite number of queens are placed
    def rQueens(board, current, size):
        if (current == size):
            return True
        else:
            for i in range(size):
                board[current] = i
                if (noConflicts(board, current)):
                    done = rQueens(board, current + 1, size)
                    if (done):
                        return True
            return False

#
#     def solve_n_queens(row):
#         if row == n:
#             result.append(col_placement.copy())
#             return
#         for col in range(n):
#             if all(
#                     abs(c - col) not in (0, row - i)
#                     for i, c in enumerate(col_placement[:row])):
#                 col_placement[row] = col
#                 solve_n_queens(row + 1)
#     result: List[List[int]] = []
#     col_placement = [0] * n
#     solve_n_queens(0)
#     return result


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('n_queens.py', 'n_queens.tsv', n_queens,
                                       comp))
