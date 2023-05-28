from dataclasses import dataclass
from heap import MaxHeap


@dataclass
class Beehive:
    """A beehive has a position in 3d space, and some stats."""

    x: int
    y: int
    z: int

    capacity: int
    nutrient_factor: int
    volume: int = 0

    def __gt__(self, other):
        """
        Best case = Worst case: O(1)
        """
        if isinstance(other, Beehive):
            if self.capacity <= self.volume:
                self_val = self.capacity * self.nutrient_factor
            else:
                self_val = self.volume * self.nutrient_factor
            if other.capacity <= other.volume:
                other_val = other.capacity * other.nutrient_factor
            else:
                other_val = other.volume * other.nutrient_factor
            return self_val > other_val

    def __le__(self, other):
        """
        Best case = Worst case: O(1)
        """
        if isinstance(other, Beehive):
            if self.capacity <= self.volume:
                self_val = self.capacity * self.nutrient_factor
            else:
                self_val = self.volume * self.nutrient_factor
            if other.capacity <= other.volume:
                other_val = other.capacity * other.nutrient_factor
            else:
                other_val = other.volume * other.nutrient_factor
            return self_val <= other_val


class BeehiveSelector:

    def __init__(self, max_beehives: int):
        """
        Best case = Worst case: O(n) where n is the max_beehives. This is because MaxHeap uses ArrayR which costs O(n)
        to be initialised
        """
        self.heap = MaxHeap(max_beehives)

    def set_all_beehives(self, hive_list: list[Beehive]):
        """
        Best case = Worst case: O(M) where M is the length of the hive_list
        """
        if not self.heap.length == 0:
            self.heap = self.__init__(len(hive_list))
        for i in hive_list:
            self.add_beehive(i)

    def add_beehive(self, hive: Beehive):
        """
        Best case: O(1) when the hive is smaller than or equal to its parent
        Worst case: O(log n) when the hive has to rise all the way to the top
        """
        self.heap.add(hive)

    def harvest_best_beehive(self) -> float:
        """
        Best case: O(1), when the hive is greater than or equal to one of its children
        Worst case: O(log n) when the hive has to sink all the way to the bottom and also due to add_behive, where the
        hive has to rise all the way to the top
        """
        hive: Beehive = self.heap.get_max()
        amount = min(hive.capacity, hive.volume)
        nutrition = hive.nutrient_factor

        if hive.volume - hive.capacity > 0:
            hive.volume = hive.volume - hive.capacity
            self.add_beehive(hive)

        return amount*nutrition
