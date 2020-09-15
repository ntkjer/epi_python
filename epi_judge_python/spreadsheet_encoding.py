from test_framework import generic_test

import functools

def ss_decode_col_id_approach(col: str) -> int:
    keys = [x for x in range(1, 27)]
    start_char = 'A'
    d = {}
    for i, key in enumerate(keys):
        d[chr(ord(start_char) + i)] = key

    result = 0
    for k in range(len(col)):
        current_char = col[k]
        result += d[current_char]

    return result


def ss_decode_col_id(col: str) -> int:
    return functools.reduce(
        lambda result, c: result * 26 + ord(c) - ord('A') + 1, col, 0)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spreadsheet_encoding.py',
                                       'spreadsheet_encoding.tsv',
                                       ss_decode_col_id))
