from test_framework import generic_test


def power(x: float, y: int) -> float:
    """
    If lsb of y is 0, result is x^y/2 *2 otherwise its x * (x^y/2)^2
    """
    result, power = 1.0, y
    if y < 0:
        power, x = -power, 1.0 / x
    while power:
        if power & 1:
            result *= x
        x, power = x * x, power >> 1
    return result


if __name__ == '__main__':
    exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv',
                                        power))
