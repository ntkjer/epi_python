from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def stable_sort_list(L: ListNode) -> Optional[ListNode]:
    # base case
    if L is None or L.next is None:
        return L

    # find midpoint
    slow, fast = L, L
    prev = None
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    if prev:
        prev.next = None

    return merge_two_sorted_lists(stable_sort_list(L), stable_sort_list(slow))


def merge_two_sorted_lists(L1: ListNode, L2: ListNode) -> ListNode:
    dummy_head = tail = ListNode()
    while L1 and L2:
        if L1.data <= L2.data:
            tail.next, L1 = L1, L1.next
        else:
            tail.next, L2 = L2, L2.next
        tail = tail.next
    tail.next = L1 or L2
    return dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sort_list.py', 'sort_list.tsv',
                                       stable_sort_list))
