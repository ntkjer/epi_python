from test_framework import generic_test

import collections

def is_letter_constructible_from_magazine(letter_text: str,
                                          magazine_text: str) -> bool:
    if len(letter_text) > len(magazine_text):
        return False

    letter_freq = collections.Counter(letter_text)
    # iterate over magazine
    # if we found a letter, decrement count
    # if count == 0, remove from dict
    # return true if len(letters) == 0
    for c in magazine_text:
        if c in letter_freq:
            letter_freq[c] -= 1
            if letter_freq[c] == 0:
                del letter_freq[c]
            if not letter_freq:
                return True
    return not letter_freq



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_anonymous_letter_constructible.py',
            'is_anonymous_letter_constructible.tsv',
            is_letter_constructible_from_magazine))
