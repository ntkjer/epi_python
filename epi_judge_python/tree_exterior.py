import functools
from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def exterior_binary_tree(tree: BinaryTreeNode) -> List[BinaryTreeNode]:
    def left_exterior(subtree):
        if not subtree or (not subtree.left and not subtree.right):
            return
        exterior.append(subtree)
        if subtree.left:
            left_exterior(subtree.left)
        else:
            left_exterior(subtree.right)

    def right_exterior(subtree):
        if not subtree or (not subtree.left and not subtree.right):
            return
        if subtree.right:
            right_exterior(subtree.right)
        else:
            right_exterior(subtree.left)
        exterior.append(subtree)

    def leaves(subtree):
        if not subtree:
            return
        if not subtree.left and not subtree.right:
            exterior.append(subtree)
        leaves(subtree.left)
        leaves(subtree.right)

    if not tree:
        return []

    exterior = [tree]
    left_exterior(tree.left)
    leaves(tree.left)
    leaves(tree.right)
    right_exterior(tree.right)
    return exterior


def create_output_list(L):
    if any(l is None for l in L):
        raise TestFailure('Resulting list contains None')
    return [l.data for l in L]


@enable_executor_hook
def create_output_list_wrapper(executor, tree):
    result = executor.run(functools.partial(exterior_binary_tree, tree))

    return create_output_list(result)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_exterior.py', 'tree_exterior.tsv',
                                       create_output_list_wrapper))
