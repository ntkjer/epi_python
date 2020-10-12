from typing import List

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test


def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    prev, result = None, []
    while tree:
        if prev is tree.parent:
            # We came down to tree from parent
            if tree.left:
                next = tree.left
            else:
                result.append(tree.data)
                # added the left-most subtree
                # go right if its not empty or go up
                next = tree.right or tree.parent
        elif tree.left is prev:
            # We came up to the tree from its left child
            result.append(tree.data)
            # left is done, go right or go up
            next = tree.right or tree.parent
        else:
            # Both children are added, lets go up
            next = tree.parent
        prev, tree = tree, next
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_with_parent_inorder.py',
                                       'tree_with_parent_inorder.tsv',
                                       inorder_traversal))
