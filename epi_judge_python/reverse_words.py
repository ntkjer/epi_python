import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Assume s is a list of strings, each of which is of length 1, e.g.,
# ['r', 'a', 'm', ' ', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y'].
def reverse_words(s):
    def reverse_section(section, start, end):
        while start < end:
            section[start], section[end] = section[end], section[start]
            start, end = start + 1, end - 1

    # Reverse the whole string s
    reverse_section(s, 0, len(s) - 1)

    # Find a start and stop pos for each word and reverse each word.
    start = 0
    while True:
        end = start
        while end < len(s) and s[end] != " ":
            end += 1
        if end == len(s):
            break
        reverse_section(s, start, end - 1)
        start = end + 1

    # Reverse the last word in the sequence
    reverse_section(s, start, len(s) - 1)


@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = list(s)

    executor.run(functools.partial(reverse_words, s_copy))

    return ''.join(s_copy)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_words.py', 'reverse_words.tsv',
                                       reverse_words_wrapper))
