from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def sum_root_to_leaf(tree: BinaryTreeNode) -> int:
    def partial_sum_helper(tree: BinaryTreeNode, partial_sum=0):
        if not tree:
            return 0
        partial_sum = partial_sum * 2 + tree.data
        if not tree.left and not tree.right:
            return partial_sum
        return (partial_sum_helper(tree.left, partial_sum) +
                partial_sum_helper(tree.right, partial_sum))
    return partial_sum_helper(tree)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sum_root_to_leaf.py',
                                       'sum_root_to_leaf.tsv',
                                       sum_root_to_leaf))
