from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_symmetric(tree: BinaryTreeNode) -> bool:
    def check_symmetric(subtree_a, subtree_b) -> bool:
        if not subtree_a and not subtree_b:
            return True
        elif subtree_a and subtree_b:
            return (subtree_a.data == subtree_b.data
                    and check_symmetric(subtree_a.left, subtree_b.right)
                    and check_symmetric(subtree_a.right, subtree_b.left))
        return False
    return not tree or check_symmetric(tree.left, tree.right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
