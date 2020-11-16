from typing import List

from test_framework import generic_test


def n_queens(n: int) -> List[List[int]]:
    def place_queen(row, board):
        if row == n:
            result.append(board[:])
            return
        for col in range(n):
            if col in cols or (col - row) in upper_diag or (col + row) in lower_diag:
                continue
            lower_diag.add(row + col)
            upper_diag.add(row - col)
            cols.add(col)

            #board[row] = "." * col + "Q" + "." * (n - col - 1)
            board[row] = [0] * col + [1] + [0] * (n - col - 1)
            print(board[row])

            place_queen(row + 1, board)

            lower_diag.remove(row + col)
            upper_diag.remove(row - col)
            cols.remove(col)

            board[row] = [0] * n
            print(board[row])


    result: List[List[int]] = []
    lower_diag, upper_diag, cols = set(), set(), set()
    board = [[0 * n] for i in range(n)]
    place_queen(0, board)
    return result

def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('n_queens.py', 'n_queens.tsv', n_queens,
                                       comp))
