from __future__ import annotations
from typing import Generic, TypeVar, Tuple
from dataclasses import dataclass, field

I = TypeVar('I')
Point = Tuple[int, int, int]


@dataclass
class BeeNode:
    key: Point
    item: I
    x_y_z: BeeNode | None = None
    x_y_nz: BeeNode | None = None
    x_ny_z: BeeNode | None = None
    x_ny_nz: BeeNode | None = None
    nx_y_z: BeeNode | None = None
    nx_ny_z: BeeNode | None = None
    nx_y_nz: BeeNode | None = None
    nx_ny_nz: BeeNode | None = None
    subtree_size: int = 1

    def get_child_for_key(self, point: Point) -> BeeNode | None:
        if point[0] > self.key[0] and point[1] > self.key[1] and point[2] > self.key[2]:
            return self.x_y_z
        elif point[0] > self.key[0] and point[1] > self.key[1] and point[2] < self.key[2]:
            return self.x_y_nz
        elif point[0] > self.key[0] and point[1] < self.key[1] and point[2] > self.key[2]:
            return self.x_ny_z
        elif point[0] > self.key[0] and point[1] < self.key[1] and point[2] < self.key[2]:
            return self.x_ny_nz
        elif point[0] < self.key[0] and point[1] > self.key[1] and point[2] > self.key[2]:
            return self.nx_y_z
        elif point[0] < self.key[0] and point[1] < self.key[1] and point[2] > self.key[2]:
            return self.nx_ny_z
        elif point[0] < self.key[0] and point[1] > self.key[1] and point[2] < self.key[2]:
            return self.nx_y_nz
        elif point[0] < self.key[0] and point[1] < self.key[1] and point[2] < self.key[2]:
            return self.nx_ny_nz
        else:
            return None


class ThreeDeeBeeTree(Generic[I]):
    """ 3️⃣🇩🐝🌳 tree. """

    def __init__(self) -> None:
        """
            Initialises an empty 3DBT
        """
        self.root = None
        self.length = 0

    def is_empty(self) -> bool:
        """
            Checks to see if the 3DBT is empty
        """
        return len(self) == 0

    def __len__(self) -> int:
        """ Returns the number of nodes in the tree. """

        return self.length

    def __contains__(self, key: Point) -> bool:
        """
            Checks to see if the key is in the 3DBT
        """
        try:
            self.get_tree_node_by_key(key)
            return True
        except KeyError:
            return False

    def __getitem__(self, key: Point) -> I:
        """
            Attempts to get an item in the tree, it uses the Key to attempt to find it
        """
        node = self.get_tree_node_by_key(key)
        return node.item

    def get_tree_node_by_key(self, key: Point) -> BeeNode:
        return self.get_tree_node_by_key_aux(self.root, key)

    def get_tree_node_by_key_aux(self, current: BeeNode, key: Point) -> BeeNode:
        if current is None:
            raise KeyError('Key not found: {0}'.format(key))
        elif key == current.key:
            return current
        elif key[0] > current.key[0] and key[1] > current.key[1] and key[2] > current.key[2]:
            return self.get_tree_node_by_key_aux(current.x_y_z, key)
        elif key[0] > current.key[0] and key[1] > current.key[1] and key[2] < current.key[2]:
            return self.get_tree_node_by_key_aux(current.x_y_nz, key)
        elif key[0] > current.key[0] and key[1] < current.key[1] and key[2] < current.key[2]:
            return self.get_tree_node_by_key_aux(current.x_ny_nz, key)
        elif key[0] < current.key[0] and key[1] < current.key[1] and key[2] < current.key[2]:
            return self.get_tree_node_by_key_aux(current.nx_ny_nz, key)
        elif key[0] > current.key[0] and key[1] < current.key[1] and key[2] > current.key[2]:
            return self.get_tree_node_by_key_aux(current.x_ny_z, key)
        elif key[0] < current.key[0] and key[1] < current.key[1] and key[2] > current.key[2]:
            return self.get_tree_node_by_key_aux(current.nx_ny_z, key)
        elif key[0] < current.key[0] and key[1] > current.key[1] and key[2] < current.key[2]:
            return self.get_tree_node_by_key_aux(current.nx_y_nz, key)
        else:
            return self.get_tree_node_by_key_aux(current.nx_y_z, key)

    def __setitem__(self, key: Point, item: I) -> None:
        self.root = self.insert_aux(self.root, key, item)

    def insert_aux(self, current: BeeNode, key: Point, item: I) -> BeeNode:
        """
            Attempts to insert an item into the tree, it uses the Key to insert it
        """
        if current is None:  # base case: at the leaf
            current = BeeNode(key, item=item)
            self.length += 1
        elif key[0] > current.key[0] and key[1] > current.key[1] and key[2] > current.key[2]:
            current.subtree_size += 1
            current.x_y_z = self.insert_aux(current.x_y_z, key, item)
        elif key[0] > current.key[0] and key[1] > current.key[1] and key[2] < current.key[2]:
            current.subtree_size += 1
            current.x_y_nz = self.insert_aux(current.x_y_nz, key, item)
        elif key[0] > current.key[0] and key[1] < current.key[1] and key[2] < current.key[2]:
            current.subtree_size += 1
            current.x_ny_nz = self.insert_aux(current.x_ny_nz, key, item)
        elif key[0] < current.key[0] and key[1] < current.key[1] and key[2] < current.key[2]:
            current.subtree_size += 1
            current.nx_ny_nz = self.insert_aux(current.nx_ny_nz, key, item)
        elif key[0] > current.key[0] and key[1] < current.key[1] and key[2] > current.key[2]:
            current.subtree_size += 1
            current.x_ny_z = self.insert_aux(current.x_ny_z, key, item)
        elif key[0] < current.key[0] and key[1] < current.key[1] and key[2] > current.key[2]:
            current.subtree_size += 1
            current.nx_ny_z = self.insert_aux(current.nx_ny_z, key, item)
        elif key[0] < current.key[0] and key[1] > current.key[1] and key[2] < current.key[2]:
            current.subtree_size += 1
            current.nx_y_nz = self.insert_aux(current.nx_y_nz, key, item)
        elif key[0] < current.key[0] and key[1] > current.key[1] and key[2] > current.key[2]:
            current.subtree_size += 1
            current.nx_y_z = self.insert_aux(current.nx_y_z, key, item)
        else:  # key == current.key
            raise ValueError('Inserting duplicate item')
        return current

    def is_leaf(self, current: BeeNode) -> bool:
        """ Simple check whether or not the node is a leaf. """
        return current.subtree_size == 1


if __name__ == "__main__":
    tdbt = ThreeDeeBeeTree()
    tdbt[(3, 3, 3)] = "A"
    tdbt[(1, 5, 2)] = "B"
    tdbt[(4, 3, 1)] = "C"
    tdbt[(5, 4, 0)] = "D"
    print(tdbt.root.get_child_for_key((4, 3, 1)).subtree_size)  # 2
