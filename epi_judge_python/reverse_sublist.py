from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:
    # Create dummy nodes
    dummy_head = sublist_head = ListNode(0, L)

    # Advance sublist_head pointer to the correct location
    for _ in range(1, start):
        sublist_head = sublist_head.next

    # Reverse sublist
    sublist_iter = sublist_head.next
    for _ in range(finish - start):
        tmp = sublist_iter.next

        sublist_iter.next = tmp.next
        tmp.next = sublist_head.next
        sublist_head.next = tmp

    return dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
