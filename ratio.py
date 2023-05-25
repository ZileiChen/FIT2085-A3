from __future__ import annotations
from typing import Generic, TypeVar
from math import ceil, floor
from bst import BinarySearchTree
from node import TreeNode

T = TypeVar("T")
I = TypeVar("I")

class Percentiles(Generic[T]):

    def __init__(self) -> None:
        # Using binary search tree to implement methods
        self.tree = BinarySearchTree()
    
    def add_point(self, item: T):
        # Using binary search tree to insert
        self.tree[item] = [item]
    
    def remove_point(self, item: T):
        # Using binary search tree to remove
        del self.tree[item]

    def ratio(self, x, y) -> list:
        x_index = ceil(x/100 * len(self.tree)) + 1
        y_index = len(self.tree) - ceil(y/100 * len(self.tree))
        xth_element = self.tree.kth_smallest(x_index, self.tree.root).item
        yth_element = self.tree.kth_smallest(y_index, self.tree.root).item
        result = []
        self.modified_inorder_traversal(self.tree.root, xth_element, yth_element, result)
        return result

    def modified_inorder_traversal(self, current_node: TreeNode, x: int, y: int, inorder_list: list):
        if current_node is not None:
            if x < current_node.item:
                self.modified_inorder_traversal(current_node.left, x, y, inorder_list)
            if x <= current_node.item <= y:
                inorder_list.append(current_node.key)
            if y > current_node.item:
                self.modified_inorder_traversal(current_node.right, x, y, inorder_list)


if __name__ == "__main__":
    points = list(range(50))
    import random
    random.shuffle(points)
    p = Percentiles()
    for point in points:
        p.add_point(point)
    # Numbers from 8 to 16.
    print(p.ratio(15, 66))
