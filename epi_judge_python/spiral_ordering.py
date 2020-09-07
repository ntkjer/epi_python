from typing import List

from test_framework import generic_test


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    shift = ((0, 1), (1, 0), (0, -1), (-1, 0))
    direction = x = y = 0
    spiral_ordering = []
    n = len(square_matrix)
    for _ in range(n ** 2):
        spiral_ordering.append(square_matrix[x][y])
        square_matrix[x][y] = 0
        next_x, next_y = x + shift[direction][0], y + shift[direction][1]
        if (next_x not in range(len(square_matrix))
                or next_y not in range(len(square_matrix))
                or square_matrix[next_x][next_y] == 0):
            direction = (direction + 1) & 3
            next_x, next_y = x + shift[direction][0], y + shift[direction][1]
        x, y = next_x, next_y
    return spiral_ordering


def matrix_in_spiral_order_book(square_matrix: List[List[int]]) -> List[int]:
    def matrix_layer_clockwise_order(offest):
        if offset == len(square_matrix) - offset - 1:
            # square_matrix has an odd dimension and we are at the center
            spiral_ordering.append(square_matrix[offset][offset])
            return
        spiral_ordering.extend(square_matrix[offest][offset:-1 - offset])
        spiral_ordering.extend(
            list(zip(*square_matrix))[-1 - offest][offset:-1 - offest])
        spiral_ordering.extend(square_matrix[-1 - offset][-1 - offset:offset:-1])
        spiral_ordering.extend(list(zip(*square_matrix))[offset][-1 - offset:offset:-1])
    spiral_ordering: List[int] = []
    for offset in range((len(square_matrix) + 1) // 2):
        print("offset: ", offset)
        matrix_layer_clockwise_order(offset)
    return spiral_ordering


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
