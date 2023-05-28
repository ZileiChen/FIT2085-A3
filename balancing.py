from __future__ import annotations

from math import ceil

from ratio import Percentiles
from threedeebeetree import Point


def make_ordering(my_coordinate_list: list[Point]) -> list[Point]:
    """
    This method recursively calls the make_ordering_aux method.
    Complexity: O(N*log(N)*log(N))
    """
    px = Percentiles()
    py = Percentiles()
    pz = Percentiles()

    solution = []
    make_ordering_aux(my_coordinate_list, solution, px, py, pz)
    return solution


def make_ordering_aux(subsection: list, solution: list, px: Percentiles, py: Percentiles, pz: Percentiles):
    """
    The algorithm for this method involves first checking if the current size of the subsection or number of points to
    be added to this subtree is less than 9. If it is, then it is added to the solution using the list extend() method
    which has a time complexity of O(N), but this method isn't always called since most of the time the list is very
    large.
    It then clears the Percentiles class trees which has a complexity of O(1)
    The points in the subsection or subtree is then added to the Percentiles classes using their x, y, and z
    coordinates as keys. Which has a complexity of O(N*log(N))
    The ratio method follows, which has a complexity of O(log(N) + O) where O is the number of points returned.
    Since the number of points returned is always 75% of N, the complexity can be written as O(log(N)+0.75N).
    We then choose a root for this subtree which is done using the intersection method from sets. This has a complexity
    of O(min(a, b, c)) where a, b and c are the sizes of these sets. Since the sizes of these sets is equal to 0.75N,
    the complexity if O(0.75N).
    We then sort the remaining points into 8 further subsections/subtrees which has a complexity of O(N).
    We finally then call this method recursively.

    Overall, the complexity for 1 iteration of this recursive algorithm is O(N+1+log(N)+log(N)+0.75N+0.75N+N)
    Which simplifies to O(N*log(N)+log(N)+N)
    By considering a large input and the overall complexities of this algorithm, this recursive algorithm divides into
    8 separate smaller algorithms. Hence, the recursion runs logarithmically O(log(N)) in terms of how many times it is
    called for any given input.
    Thus, the final complexity is given as O((N*log(N)+log(N)+N)*log(N)) = O(N*log(N)*log(N)) since the log-linear
    complexity will dominate the time complexity as N increases.
    """
    if len(subsection) <= 9:
        solution.extend(subsection)
        return

    px.clear()
    py.clear()
    pz.clear()

    for point in subsection:
        px.add_point_key_value(point[0], point)
        py.add_point_key_value(point[1], point)
        pz.add_point_key_value(point[2], point)
    potential_root_x = px.ratio(12.5, 12.5)
    potential_root_y = py.ratio(12.5, 12.5)
    potential_root_z = pz.ratio(12.5, 12.5)

    candidates = list(set(potential_root_x).intersection(potential_root_y).intersection(potential_root_z))
    median = len(candidates) // 2
    chosen_root = candidates[median]
    subsection.remove(chosen_root)
    solution.append(chosen_root)

    ppp = []
    ppn = []
    pnp = []
    pnn = []
    npp = []
    npn = []
    nnp = []
    nnn = []

    for point in subsection:
        if point[0] > chosen_root[0] and point[1] > chosen_root[1] and point[2] > chosen_root[2]:
            ppp.append(point)
        elif point[0] > chosen_root[0] and point[1] > chosen_root[1] and point[2] < chosen_root[2]:
            ppn.append(point)
        elif point[0] > chosen_root[0] and point[1] < chosen_root[1] and point[2] > chosen_root[2]:
            pnp.append(point)
        elif point[0] > chosen_root[0] and point[1] < chosen_root[1] and point[2] < chosen_root[2]:
            pnn.append(point)
        elif point[0] < chosen_root[0] and point[1] > chosen_root[1] and point[2] > chosen_root[2]:
            npp.append(point)
        elif point[0] < chosen_root[0] and point[1] > chosen_root[1] and point[2] < chosen_root[2]:
            npn.append(point)
        elif point[0] < chosen_root[0] and point[1] < chosen_root[1] and point[2] > chosen_root[2]:
            nnp.append(point)
        elif point[0] < chosen_root[0] and point[1] < chosen_root[1] and point[2] < chosen_root[2]:
            nnn.append(point)

    make_ordering_aux(ppp, solution, px, py, pz)
    make_ordering_aux(ppn, solution, px, py, pz)
    make_ordering_aux(pnp, solution, px, py, pz)
    make_ordering_aux(pnn, solution, px, py, pz)
    make_ordering_aux(npp, solution, px, py, pz)
    make_ordering_aux(npn, solution, px, py, pz)
    make_ordering_aux(nnp, solution, px, py, pz)
    make_ordering_aux(nnn, solution, px, py, pz)

