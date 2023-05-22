from __future__ import annotations
from typing import Generic, TypeVar
from math import ceil
from bst import BinarySearchTree

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

    def ratio(self, x, y):
        
        # use binary search for the lower and upper values


if __name__ == "__main__":
    points = list(range(50))
    import random
    random.shuffle(points)
    p = Percentiles()
    for point in points:
        p.add_point(point)
    # Numbers from 8 to 16.
    print(p.ratio(15, 66))
