from test_framework import generic_test


def roman_to_integer(s: str) -> int:
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    # Set result as value of last letter
    result = values[s[len(s) - 1]]
    for i in range(len(s) - 1, 0, -1):
        cur = values[s[i]]
        prev = values[s[i - 1]]
        if prev >= cur:
            result += prev
        else:
            # IX -> X = 10, I = 1, subtract 1 from 10
            result -= prev
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('roman_to_integer.py',
                                       'roman_to_integer.tsv',
                                       roman_to_integer))
