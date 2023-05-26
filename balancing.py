from __future__ import annotations

from math import ceil

from ratio import Percentiles
from threedeebeetree import Point

def make_ordering(my_coordinate_list: list[Point]) -> list[Point]:
    px = Percentiles()
    py = Percentiles()
    pz = Percentiles()
    factor = 12.5
    for coordinate in my_coordinate_list:
        px.add_point_key_value(coordinate[0], coordinate)
        py.add_point_key_value(coordinate[1], coordinate)
        pz.add_point_key_value(coordinate[2], coordinate)

    complete_x = px.ratio(0, 0)
    complete_y = py.ratio(0, 0)
    complete_z = pz.ratio(0, 0)

    solution = []
    make_ordering_aux(solution, px, py, pz, [0, 0], [0, 0], [0, 0], complete_x, complete_y, complete_z)
    return solution

def make_ordering_aux(solution_list: list, x: Percentiles, y: Percentiles, z: Percentiles, x_range: list, y_range: list, z_range: list, x_sorted, y_sorted, z_sorted):
    relative_factor_x = (100 - x_range[1] - x_range[0]) * 12.5 / 100
    relative_factor_y = (100 - y_range[1] - y_range[0]) * 12.5 / 100
    relative_factor_z = (100 - z_range[1] - z_range[0]) * 12.5 / 100

    x_candidate = x.ratio(x_range[0], x_range[1])
    y_candidate = y.ratio(y_range[0], y_range[1])
    z_candidate = z.ratio(z_range[0], z_range[1])

    if min(len(x_candidate), len(y_candidate), len(z_candidate)) < 17:
        #add the rest of the points to the solution list in any order
        for coord in x_candidate:
            solution_list.append(coord)
        for coord in y_candidate:
            if y_candidate.__contains__(coord):
                solution_list.append(coord)
        for coord in z_candidate:
            if z_candidate.__contains__(coord):
                solution_list.append(coord)
        return
    else:
        x_candidate = x_candidate[ceil(12.5/100 * len(x_candidate)) + 1 : len(x_candidate) - ceil(12.5/100 * len(x_candidate))]
        y_candidate = y_candidate[ceil(12.5/100 * len(y_candidate)) + 1 : len(y_candidate) - ceil(12.5/100 * len(y_candidate))]
        z_candidate = z_candidate[ceil(12.5/100 * len(z_candidate)) + 1 : len(z_candidate) - ceil(12.5/100 * len(z_candidate))]



    candidates = list(set(x_candidate).intersection(y_candidate).intersection(z_candidate))



    x_index = x_sorted.index(candidates[0])
    y_index = y_sorted.index(candidates[0])
    z_index = z_sorted.index(candidates[0])
    solution_list.append(candidates[0])
    x.remove_point(candidates[0])
    y.remove_point(candidates[0])
    z.remove_point(candidates[0])

    # +x, +y, +z
    x_range = [x_index * 100 / len(x_candidate), x_range[1]]
    y_range = [y_index * 100 / len(y_candidate), y_range[1]]
    z_range = [z_index * 100 / len(z_candidate), z_range[1]]
    make_ordering_aux(solution_list, x, y, z, x_range, y_range, z_range)

    # +x, +y, -z
    x_range = [x_index * 100 / len(x_candidate), x_range[1]]
    y_range = [y_index * 100 / len(y_candidate), y_range[1]]
    z_range = [z_range[0], z_index * 100 / len(z_candidate)]
    make_ordering_aux(solution_list, x, y, z, x_range, y_range, z_range)

    # +x, -y, +z
    x_range = [x_index * 100 / len(x_candidate), x_range[1]]
    y_range = [y_range[0], y_index * 100 / len(y_candidate)]
    z_range = [z_index * 100 / len(z_candidate), z_range[1]]
    make_ordering_aux(solution_list, x, y, z, x_range, y_range, z_range)

    # -x, +y, +z
    x_range = [x_range[0], x_index * 100 / len(x_candidate)]
    y_range = [y_index * 100 / len(y_candidate), y_range[1]]
    z_range = [z_index * 100 / len(z_candidate), z_range[1]]
    make_ordering_aux(solution_list, x, y, z, x_range, y_range, z_range)

    # +x, -y, -z
    x_range = [x_index * 100 / len(x_candidate), x_range[1]]
    y_range = [y_range[0], y_index * 100 / len(y_candidate)]
    z_range = [z_range[0], z_index * 100 / len(z_candidate)]
    make_ordering_aux(solution_list, x, y, z, x_range, y_range, z_range)

    # -x, -y, +z
    x_range = [x_range[0], x_index * 100 / len(x_candidate)]
    y_range = [y_range[0], y_index * 100 / len(y_candidate)]
    z_range = [z_index * 100 / len(z_candidate), z_range[1]]
    make_ordering_aux(solution_list, x, y, z, x_range, y_range, z_range)

    # -x, +y, -z
    x_range = [x_range[0], x_index * 100 / len(x_candidate)]
    y_range = [y_index * 100 / len(y_candidate), y_range[1]]
    z_range = [z_range[0], z_index * 100 / len(z_candidate)]
    make_ordering_aux(solution_list, x, y, z, x_range, y_range, z_range)

    # -x, -y, -z
    x_range = [x_range[0], x_index * 100 / len(x_candidate)]
    y_range = [y_range[0], y_index * 100 / len(y_candidate)]
    z_range = [z_range[0], z_index * 100 / len(z_candidate)]
    make_ordering_aux(solution_list, x, y, z, x_range, y_range, z_range)