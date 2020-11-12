from typing import List, Optional

from bst_node import BstNode
from test_framework import generic_test


def rebuild_bst_from_preorder(preorder_sequence: List[int]
                              ) -> Optional[BstNode]:
    def rebuild_bst_from_preorder_on_value_range(lower_bound, upper_bound):
        if root_idx[0] == len(preorder_sequence):
            return None
        root = preorder_sequence[root_idx[0]]
        if not lower_bound <= root <= upper_bound:
            return None
        root_idx[0] += 1
        # this method updates root_idx[0
        # the order of calls below is important
        left_subtree = rebuild_bst_from_preorder_on_value_range(lower_bound, root)
        right_subtree = rebuild_bst_from_preorder_on_value_range(root, upper_bound)
        return BstNode(root, left_subtree, right_subtree)
    root_idx = [0]
    return rebuild_bst_from_preorder_on_value_range(float('-inf'), float('inf'))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('bst_from_preorder.py',
                                       'bst_from_preorder.tsv',
                                       rebuild_bst_from_preorder))
