from test_framework import generic_test


def is_well_formed(s: str) -> bool:
    lookup = {"{": "}",
              "[": "]",
              "(": ")"}
    left_chars = []
    for c in s:
        if c in lookup:
            left_chars.append(c)
        elif not left_chars or lookup[left_chars.pop()] != c:
            return False
    # if stack is not empty we have unmatched chars in s
    return not left_chars


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_parenthesization.py',
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
