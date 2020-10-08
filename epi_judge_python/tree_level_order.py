from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

import collections

def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    result: List[List[int]] = []
    if not tree:
        return result

    queue = collections.deque()
    queue.append(tree)
    while queue:
        depth = len(queue)
        current_level = []
        for i in range(depth):
            current = queue.popleft()
            current_level.append(current.data)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        result.append(current_level)
    return result


def binary_tree_depth_order_2(tree: BinaryTreeNode) -> List[List[int]]:
    result: List[List[int]] = []
    if not tree:
        return result

    curr_node_depth = [tree]
    while curr_node_depth:
        result.append([curr.data for curr in curr_node_depth])
        curr_node_depth = [
            child for curr in curr_node_depth
            for child in (curr.left, curr.right) if child
        ]

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_level_order.py',
                                       'tree_level_order.tsv',
                                       binary_tree_depth_order))
