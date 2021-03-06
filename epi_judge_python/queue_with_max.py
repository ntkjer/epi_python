from test_framework import generic_test
from test_framework.test_failure import TestFailure

import collections
from typing import Deque

class QueueWithMax:

    def __init__(self) -> None:
        self._entries: Deque[any] = collections.deque()
        self._max_candidates: Deque[any] = collections.deque()

    def enqueue(self, x: int) -> None:
        self._entries.append(x)
        while self._max_candidates and self._max_candidates[-1] < x:
            self._max_candidates.pop()
        self._max_candidates.append(x)

    def dequeue(self) -> int:
        if self._entries:
            result = self._entries.popleft()
            if result is self._max_candidates[0]:
                self._max_candidates.popleft()
            return result
        raise ValueError('empty queue.')


    def dequeue_brute_force(self) -> int:
        """
        Brute force O(m) where m is the number of
        queued items we check to update new max.
        """
        if self._entries:
            result = self._entries.popleft()
            if result is self._max:
                curr_max = self._entries[-1] if self._entries else -math.inf
                for entry in self._entries:
                    if entry >= curr_max:
                        curr_max = entry
                self._max = curr_max
            return result
        raise ValueError('Cant dequeue empty queue')

    def empty(self) -> bool:
        return len(self._entries) == 0

    def max(self) -> int:
        if self.empty():
            raise IndexError("Empty Queue has no max")
        return self._max_candidates[0]


def queue_tester(ops):

    try:
        q = QueueWithMax()

        for (op, arg) in ops:
            if op == 'QueueWithMax':
                q = QueueWithMax()
            elif op == 'enqueue':
                q.enqueue(arg)
            elif op == 'dequeue':
                result = q.dequeue()
                if result != arg:
                    raise TestFailure('Dequeue: expected ' + str(arg) +
                                      ', got ' + str(result))
            elif op == 'max':
                result = q.max()
                if result != arg:
                    raise TestFailure('Max: expected ' + str(arg) + ', got ' +
                                      str(result))
            else:
                raise RuntimeError('Unsupported queue operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('queue_with_max.py',
                                       'queue_with_max.tsv', queue_tester))
