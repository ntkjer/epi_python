from typing import Set, List

from test_framework import generic_test

import collections, string

class GraphVertex:
    def __init__(self) -> None:
        self.label = None
        self.edges = []

def transform_string(D: Set[str], s: str, t: str) -> int:
    StringWithDistance = collections.namedtuple("StringWithDistance", ("candidate_string", "distance"))
    q = collections.deque([StringWithDistance(s, 0)])
    D.remove(s)

    while q:
        f = q.popleft()
        if f.candidate_string == t:
            return f.distance

        for i in range(len(f.candidate_string)):
            for c in string.ascii_lowercase:  # a - z
                candidate = f.candidate_string[:i] + c + f.candidate_string[i + 1:]
                if candidate in D:
                    D.remove(candidate)
                    q.append(StringWithDistance(candidate, f.distance + 1))

    return -1
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_transformability.py',
                                       'string_transformability.tsv',
                                       transform_string))
