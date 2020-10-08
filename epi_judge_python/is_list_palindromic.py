from list_node import ListNode
from test_framework import generic_test


def is_linked_list_a_palindrome_bf(L: ListNode) -> bool:
    def length(L: ListNode) -> int:
        n = 1
        while L:
            n += 1
            L = L.next
        return n

    first_half = ListNode(0, L)
    second_half = ListNode(0, L)

    total_length = length(L)
    half = total_length // 2

    while half:
        half -= 1
        second_half = second_half.next

    first_half = first_half.next
    second_half = second_half.next
    while first_half and second_half:
        if first_half.data != second_half.data:
            return False
        first_half = first_half.next
        second_half = second_half.next

    return True


def reverse_list(L: ListNode) -> ListNode:
    prev = None
    current = L
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev


def is_linked_list_a_palindrome(L: ListNode) -> bool:
    slow = fast = L
    while fast and fast.next:
        fast, slow = fast.next.next, slow.next

    # slow pointer points to halved list
    first_half_iter, second_half_iter = L, reverse_list(slow)
    while second_half_iter and first_half_iter:
        if second_half_iter.data != first_half_iter.data:
            return False
        second_half_iter, first_half_iter = (second_half_iter.next,
                                             first_half_iter.next)
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_list_palindromic.py',
                                       'is_list_palindromic.tsv',
                                       is_linked_list_a_palindrome))
