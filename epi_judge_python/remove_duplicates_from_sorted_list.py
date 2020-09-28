from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def remove_duplicates(L: ListNode) -> Optional[ListNode]:
    curr = L
    while curr:
        next_node = curr.next
        while next_node and curr.data == next_node.data:
            next_node = next_node.next
        curr.next = next_node
        curr = next_node
    return L

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'remove_duplicates_from_sorted_list.py',
            'remove_duplicates_from_sorted_list.tsv', remove_duplicates))
