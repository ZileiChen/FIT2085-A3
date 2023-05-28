from __future__ import annotations
from typing import Generic, TypeVar
from math import ceil, floor
from bst import BinarySearchTree
from node import TreeNode

T = TypeVar("T")
I = TypeVar("I")

class Percentiles(Generic[T]):

    def __init__(self) -> None:
        """
            Constructor for Percentiles class.
            :complexity: O(1)
        """
        # Using binary search tree to implement methods
        self.tree = BinarySearchTree()
    
    def add_point(self, item: T):
        """
        Adds an item to the Percentiles tree using binary search tree.
        :complexity: Worst case: O(N) where n is the number of elements in the search tree and the tree has a depth
        of N.
        Best case: O(logN) where N is the number of elements in the search tree and the tree is balanced.
        However, it is assumed that all BST are bounded by a depth of log(n), the assumed worst case complexity is
        O(log(N)).
        """
        # Using binary search tree to insert
        self.tree[item] = item
    
    def remove_point(self, item: T):
        """
        Complexity: Same as add_point() method above.
        """
        # Using binary search tree to remove
        del self.tree[item]

    def ratio(self, x: int, y: int) -> list:
        """
        Complexity:
        The kth_smallest() method has a complexity of O(log(N)) where N is the number of nodes in the tree.
        The modified_inorder_traversal method is a recursive method that traverses the binary search tree in Inorder
        traversal, starting from the xth smallest element to the yth smallest element. Hence, the only nodes that are
        visited are the ones that we need as output. This leads to a complexity O(O) where O is the number of nodes
        outputted by the function.
        Hence, overall complexity of this function is O(log(N) + O)
        """
        x_index = ceil(x/100 * len(self.tree)) + 1
        y_index = len(self.tree) - ceil(y/100 * len(self.tree))
        xth_element = self.tree.kth_smallest(x_index, self.tree.root).key
        yth_element = self.tree.kth_smallest(y_index, self.tree.root).key
        result = []
        self.modified_inorder_traversal(self.tree.root, xth_element, yth_element, result)
        return result

    def modified_inorder_traversal(self, current_node: TreeNode, x: int, y: int, inorder_list: list):
        """
        This method traverses the binary search tree in Inorder traversal. However, it starts the traversal at the
        k1th smallest element and finishes at the k2th smallest element. Therefore, the complexity is O(O) where O is the
        number of nodes returned and traversed by the function.
        """
        if current_node is not None:
            if x < current_node.key:
                self.modified_inorder_traversal(current_node.left, x, y, inorder_list)
            if x <= current_node.key <= y:
                inorder_list.append(current_node.item)
            if y > current_node.key:
                self.modified_inorder_traversal(current_node.right, x, y, inorder_list)

    def add_point_key_value(self, key: T, value: T):
        """
        Modified version of add_point, which allows for adding an item with a key pair.
        Complexity O(1)
        """
        self.tree[key] = value

    def clear(self):
        """
        Removes every element in the tree.
        Complexity O(1)
        """
        self.tree.clear()


if __name__ == "__main__":
    points = list(range(50))
    import random
    random.shuffle(points)
    p = Percentiles()
    for point in points:
        p.add_point(point)
    # Numbers from 8 to 16.
    print(p.ratio(0, 0))
