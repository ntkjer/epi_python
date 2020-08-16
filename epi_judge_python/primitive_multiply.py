from test_framework import generic_test


def add(a, b):
    return a if b == 0 else add(a ^ b, (a & b) << 1)


def multiply(x: int, y: int) -> int:
    result = 0
    while x:
        if x & 1:
            result = add(result, y)
        x, y = x >> 1, y << 1
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('primitive_multiply.py',
                                       'primitive_multiply.tsv', multiply))
