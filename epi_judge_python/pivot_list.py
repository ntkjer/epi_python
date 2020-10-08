import functools
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def list_pivoting(l: ListNode, x: int) -> Optional[ListNode]:
    less_head = less_iter = ListNode()
    eq_head = eq_iter = ListNode()
    gt_head = gt_iter = ListNode()

    while l:
        if l.data < x:
            less_iter.next = l
            less_iter = less_iter.next
        elif l.data == x:
            eq_iter.next = l
            eq_iter = eq_iter.next
        else:
            gt_iter.next = l
            gt_iter = gt_iter.next
        l = l.next

    gt_iter.next = None
    eq_iter.next = gt_head.next
    less_iter.next = eq_head.next
return less_head.next

def linked_to_list(l):
    v = list()
    while l is not None:
        v.append(l.data)
        l = l.next
    return v


@enable_executor_hook
def list_pivoting_wrapper(executor, l, x):
    original = linked_to_list(l)

    l = executor.run(functools.partial(list_pivoting, l, x))

    pivoted = linked_to_list(l)
    mode = -1
    for i in pivoted:
        if mode == -1:
            if i == x:
                mode = 0
            elif i > x:
                mode = 1
        elif mode == 0:
            if i < x:
                raise TestFailure('List is not pivoted')
            elif i > x:
                mode = 1
        else:
            if i <= x:
                raise TestFailure('List is not pivoted')

    if sorted(original) != sorted(pivoted):
        raise TestFailure('Result list contains different values')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('pivot_list.py', 'pivot_list.tsv',
                                       list_pivoting_wrapper))
