from __future__ import annotations

from threedeebeetree import Point


def make_ordering(my_coordinate_list: list[Point]) -> list[Point]:
    # currently has O(n * logn) complexity
    # if can multiply this by logn, will have correct complexity
    sorted_list = sorted(my_coordinate_list)  # O(n * logn)
    x_sorted = sorted(my_coordinate_list, key=lambda x: x[0])
    result = []

    def build_tree_rec(lo, hi):
        if hi - lo < 1:
            return
        # Add median
        mid = (hi + lo) // 2
        result.append(sorted_list[mid])
        build_tree_rec(lo, mid)
        build_tree_rec(mid + 1, hi)

    build_tree_rec(0, len(sorted_list))
    return result


def summation(test_tup):
    # Converting into list
    test = list(test_tup)

    # Initializing count
    count = 0

    # for loop
    for i in test:
        count += i
    return count


'''
    test = []
    for i in range(len(my_coordinate_list)):
        test.append([i, summation(my_coordinate_list[i])])
    test_sorted = sorted(test, key=lambda x: x[1])
    result2 = []
    '''
# result2.append(my_coordinate_list[test_sorted[mid][0]])
