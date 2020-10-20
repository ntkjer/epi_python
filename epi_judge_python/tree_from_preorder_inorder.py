from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

import collections

def binary_tree_from_preorder_inorder(preorder: List[int],
                                      inorder: List[int]) -> BinaryTreeNode:
    node_to_inorder_idx = {data: i for i, data in enumerate(inorder)}
    def binary_tree_from_preorder_inorder_helper(pre_start, pre_end,
                                                 in_start, in_end):
        if pre_end <= pre_start or in_end <= in_start:
            return None
        root_inorder_idx = node_to_inorder_idx[preorder[pre_start]]
        left_subtree_size = root_inorder_idx - in_start
        return BinaryTreeNode(
            preorder[pre_start],
            # recursively build left sub-tree
            binary_tree_from_preorder_inorder_helper(
                pre_start + 1, pre_start + 1 + left_subtree_size,
                in_start, root_inorder_idx),
            # recursively build right sub-tree
            binary_tree_from_preorder_inorder_helper(
                pre_start + 1 + left_subtree_size, pre_end,
                root_inorder_idx + 1, in_end))

    return binary_tree_from_preorder_inorder_helper(pre_start=0,
                                                    pre_end=len(preorder),
                                                    in_start=0,
                                                    in_end=len(inorder))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_from_preorder_inorder.py',
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
