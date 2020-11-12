import collections
from typing import List

from bst_node import BstNode
from test_framework import generic_test

Interval = collections.namedtuple('Interval', ('left', 'right'))


def range_lookup_in_bst(tree: BstNode, interval: Interval) -> List[int]:
    # if the root.data < interval.left, we do not visit left subtree
    # if root.data > interval. right, do not visit right
    # otherwise we add the current root.data and traverse left and right subtrees
    def traverse(subtree, lo=interval.left, hi=interval.right):
        if not subtree:
            return
        current_val = subtree.data
        if lo <= current_val <= hi:
            traverse(subtree.left)
            result.append(current_val)
            traverse(subtree.right)
        elif lo > current_val:
            traverse(subtree.right)
        else:
            traverse(subtree.left)
    result = []
    traverse(tree)
    return result




def range_lookup_in_bst_wrapper(tree, i):
    return range_lookup_in_bst(tree, Interval(*i))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('range_lookup_in_bst.py',
                                       'range_lookup_in_bst.tsv',
                                       range_lookup_in_bst_wrapper))
