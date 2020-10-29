from test_framework import generic_test

import collections

def can_form_palindrome(s: str) -> bool:
    # A palindormic string can only be formed iff a
    # char appears odd number of times at most once.
    #return sum(v % 2 for v in collections.Counter(s).values()) <= 1
    counter = collections.Counter(s)
    num_odd = sum(v % 2 for v in counter.values())
    return num_odd <= 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_permutable_to_palindrome.py',
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))