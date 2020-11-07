from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

import collections

def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    # compute max key stored in left subtree, a
    # compute min key in stored in right tree, b
    # if a <= root <= b
    def are_keys_in_range(tree,
                          low_range=float('-inf'),
                          high_range=float('inf')):
        if not tree:
            return True
        elif not low_range <= tree.data <= high_range:
            return False
        return (are_keys_in_range(tree.left, low_range, tree.data)
                and are_keys_in_range(tree.right, tree.data, high_range))

    return are_keys_in_range(tree)

def is_binary_tree_bst_2(tree: BinaryTreeNode) -> bool:
    QueueEntry = collections.namedtuple('QueueEntry', ('node', 'lower', 'upper'))
    bfs_queue = collections.deque(
        [QueueEntry(tree, float('-inf'), float('inf'))])

    while bfs_queue:
        front = bfs_queue.popleft()
        if front.node:
            if not front.lower <= front.node.data <= front.upper:
                return False
            bfs_queue.extend(
                (QueueEntry(front.node.left, front.lower, front.node.data),
                 QueueEntry(front.node.right, front.node.data, front.upper)))

    return True

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
