from typing import List
import typing, time

from test_framework import generic_test

def minimum_messiness(words: List[str], line_length: int) -> int:
    # messiness/cost function:
    #     each line: b blank chars at end of line is b*b
    #     each seq: sum of all lines
    #     cant take greedy approach and pack in spaces at last line!

    # minimize messiness
    # hint: focus on last word and last line

    # M(i) = min(f(j,i) + M(j - 1))
    # f(j,i) = messiness of single line consisting of words from j to i

    num_remaining_blanks = line_length - len(words[0])
    # min_messiness[i] is the min messiness when placing words[0: i + 1]
    min_messiness = ([num_remaining_blanks**2] +
                     [typing.cast(int, float('inf'))] * (len(words) - 1))
    for i in range(1, len(words)):
        num_remaining_blanks = line_length - len(words[i])
        min_messiness[i] = min_messiness[i - 1] + num_remaining_blanks**2
        # try adding words[i - 1], words[i - 2], ...
        for j in reversed(range(i)):
            num_remaining_blanks -= len(words[j]) + 1
            if num_remaining_blanks < 0:
                # not enough space to add more words.
                break
            first_j_messiness = 0 if j - 1 < 0 else min_messiness[j - 1]
            current_line_messiness = num_remaining_blanks**2
            min_messiness[i] = min(min_messiness[i],
                                   first_j_messiness + current_line_messiness)
    return min_messiness[-1]





if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('pretty_printing.py',
                                       'pretty_printing.tsv',
                                       minimum_messiness))
