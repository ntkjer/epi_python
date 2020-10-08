from test_framework import generic_test
from test_framework.test_failure import TestFailure
from typing import List

import collections

#class Stack:
#    ElementWithCachedMax = collections.namedtuple('ElementWithCachedMax',
#                                                  ('element', 'max'))
#
#    def __init__(self) -> None:
#        self._element_with_cached_max : List[Stack.ElementWithCachedMax] = []
#
#    def empty(self) -> bool:
#        return len(self._element_with_cached_max) == 0
#
#    def max(self) -> int:
#        return self._element_with_cached_max[-1].max
#
#    def pop(self) -> int:
#        return self._element_with_cached_max.pop().element
#
#    def push(self, x: int) -> None:
#        self._element_with_cached_max.append(
#            self.ElementWithCachedMax(
#                x, x if self.empty() else max(x, self.max())))
#        return
#
class Stack:

    # store curr val and curr max at each point
    def __init__(self) -> None:
        self.stack = []

    def empty(self) -> bool:
        return len(self.stack) == 0

    def max(self) -> int:
        if self.empty():
            raise IndexError("empty stack has no max")
        return self.stack[-1][1]

    def push(self, x: int) -> None:
        if self.empty():
            self.stack.append((x, x))
        else:
            self.stack.append((x, max(x, self.max())))

    def pop(self) -> int:
        if not self.empty():
            return self.stack.pop()[0]
        raise IndexError("empty stack cant pop")


def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == 'Stack':
                s = Stack()
            elif op == 'push':
                s.push(arg)
            elif op == 'pop':
                result = s.pop()
                if result != arg:
                    raise TestFailure('Pop: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'max':
                result = s.max()
                if result != arg:
                    raise TestFailure('Max: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'empty':
                result = int(s.empty())
                if result != arg:
                    raise TestFailure('Empty: expected ' + str(arg) +
                                      ', got ' + str(result))
            else:
                raise RuntimeError('Unsupported stack operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('stack_with_max.py',
                                       'stack_with_max.tsv', stack_tester))
