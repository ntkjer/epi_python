from typing import List

from test_framework import generic_test


def fill_surrounded_regions(board: List[List[str]]) -> None:
    m, n = len(board), len(board[-1])

    def dfs(x, y):
        board[x][y] = "T"
        for x, y in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if 0 <= x < m and 0 <= y < n and board[x][y] == "W":
                dfs(x, y)

    for i in range(m):
        for j in range(n):
            if board[i][j] == "W" and (i == 0 or j == 0 or i == m - 1 or j == n - 1):
                dfs(i, j)

    board[:] = [['B' if c != 'T' else 'W' for c in row] for row in board]


def fill_surrounded_regions_wrapper(board):
    fill_surrounded_regions(board)
    return board


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_enclosed_regions.py',
                                       'matrix_enclosed_regions.tsv',
                                       fill_surrounded_regions_wrapper))
