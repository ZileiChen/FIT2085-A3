from __future__ import annotations

from math import ceil

from ratio import Percentiles
from threedeebeetree import Point

def make_ordering(my_coordinate_list: list[Point]) -> list[Point]:
    px = Percentiles()
    py = Percentiles()
    pz = Percentiles()

    solution = []
    make_ordering_aux(my_coordinate_list, solution, px, py, pz)
    return solution

def make_ordering_aux(subsection: list, solution: list, px, py, pz):
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




    # relative_factor_x = (100 - x_range[1] - x_range[0]) * 12.5 / 100
    # relative_factor_y = (100 - y_range[1] - y_range[0]) * 12.5 / 100
    # relative_factor_z = (100 - z_range[1] - z_range[0]) * 12.5 / 100
    #
    # x_candidate = x.ratio(x_range[0], x_range[1])
    # y_candidate = y.ratio(y_range[0], y_range[1])
    # z_candidate = z.ratio(z_range[0], z_range[1])
    #
    # # if len(x_candidate) <= 17:
    # #     for coord in x_candidate:
    # #         solution_list.append(coord)
    # #         x.remove_point(coord[0])
    # #         y.remove_point(coord[1])
    # #         z.remove_point(coord[2])
    # #     return
    # # elif len(y_candidate) <= 17:
    # #     for coord in y_candidate:
    # #         solution_list.append(coord)
    # #         x.remove_point(coord[0])
    # #         y.remove_point(coord[1])
    # #         z.remove_point(coord[2])
    # #     return
    # # elif len(z_candidate) <= 17:
    # #     for coord in z_candidate:
    # #         solution_list.append(coord)
    # #         x.remove_point(coord[0])
    # #         y.remove_point(coord[1])
    # #         z.remove_point(coord[2])
    # #     return
    # # else:
    # #     x_candidate = x_candidate[ceil(12.5/100 * len(x_candidate)) + 0 : len(x_candidate) - ceil(12.5/100 * len(x_candidate))]
    # #     y_candidate = y_candidate[ceil(12.5/100 * len(y_candidate)) + 0 : len(y_candidate) - ceil(12.5/100 * len(y_candidate))]
    # #     z_candidate = z_candidate[ceil(12.5/100 * len(z_candidate)) + 0 : len(z_candidate) - ceil(12.5/100 * len(z_candidate))]
    #
    # if max(len(x_candidate), len(y_candidate), len(z_candidate)) <= 17:
    #     #add the rest of the points to the solution list in any order
    #     for coord in x_candidate:
    #         solution_list.append(coord)
    #         # x.remove_point(coord[0])
    #         # y.remove_point(coord[1])
    #         # z.remove_point(coord[2])
    #     for coord in y_candidate:
    #         if not solution_list.__contains__(coord):
    #             solution_list.append(coord)
    #             # x.remove_point(coord[0])
    #             # y.remove_point(coord[1])
    #             # z.remove_point(coord[2])
    #     for coord in z_candidate:
    #         if not solution_list.__contains__(coord):
    #             solution_list.append(coord)
    #             # x.remove_point(coord[0])
    #             # y.remove_point(coord[1])
    #             # z.remove_point(coord[2])
    #     return
    # else:
    #     x_candidate = x_candidate[
    #               ceil(12.5 / 100 * len(x_candidate)) + 0: len(x_candidate) - ceil(12.5 / 100 * len(x_candidate))]
    #     y_candidate = y_candidate[
    #               ceil(12.5 / 100 * len(y_candidate)) + 0: len(y_candidate) - ceil(12.5 / 100 * len(y_candidate))]
    #     z_candidate = z_candidate[
    #               ceil(12.5 / 100 * len(z_candidate)) + 0: len(z_candidate) - ceil(12.5 / 100 * len(z_candidate))]
    #
    #
    #
    # candidates = list(set(x_candidate).intersection(y_candidate).intersection(z_candidate))
    #
    # median = len(candidates) // 2
    #
    # if len(candidates) == 0:
    #     return
    #
    # x_index = x_sorted.index(candidates[median])
    # y_index = y_sorted.index(candidates[median])
    # z_index = z_sorted.index(candidates[median])
    # solution_list.append(candidates[median])
    #
    # x.remove_point(candidates[median][0])
    # y.remove_point(candidates[median][1])
    # z.remove_point(candidates[median][2])
    #
    # # +x, -y, -z
    # x_range = [x_index * 100 / len(x_sorted), x_range[1]]
    # y_range = [y_range[0], 100 - (y_index * 100 / len(y_sorted))]
    # z_range = [z_range[0], 100 - (z_index * 100 / len(z_sorted))]
    # make_ordering_aux(solution_list, x, y, z, x_range, y_range, z_range, x_sorted, y_sorted, z_sorted)
    #
    # # -x, -y, +z
    # x_range = [x_range[0], 100 - (x_index * 100 / len(x_sorted))]
    # y_range = [y_range[0], 100 - (y_index * 100 / len(y_sorted))]
    # z_range = [z_index * 100 / len(z_sorted), z_range[1]]
    # make_ordering_aux(solution_list, x, y, z, x_range, y_range, z_range, x_sorted, y_sorted, z_sorted)
    #
    # # -x, +y, -z
    # x_range = [x_range[0], 100 - (x_index * 100 / len(x_sorted))]
    # y_range = [y_index * 100 / len(y_sorted), y_range[1]]
    # z_range = [z_range[0], 100 - (z_index * 100 / len(z_sorted))]
    # make_ordering_aux(solution_list, x, y, z, x_range, y_range, z_range, x_sorted, y_sorted, z_sorted)
    #
    # # -x, -y, -z
    # x_range = [x_range[0], 100 - (x_index * 100 / len(x_sorted))]
    # y_range = [y_range[0], 100 - (y_index * 100 / len(y_sorted))]
    # z_range = [z_range[0], 100 - (z_index * 100 / len(z_sorted))]
    # make_ordering_aux(solution_list, x, y, z, x_range, y_range, z_range, x_sorted, y_sorted, z_sorted)
    #
    #
    # # +x, +y, +z
    # x_range = [x_index * 100 / len(x_sorted), x_range[1]]
    # y_range = [y_index * 100 / len(y_sorted), y_range[1]]
    # z_range = [z_index * 100 / len(z_sorted), z_range[1]]
    # make_ordering_aux(solution_list, x, y, z, x_range, y_range, z_range, x_sorted, y_sorted, z_sorted)
    #
    # # +x, +y, -z
    # x_range = [x_index * 100 / len(x_sorted), x_range[1]]
    # y_range = [y_index * 100 / len(y_sorted), y_range[1]]
    # z_range = [z_range[0], 100 - (z_index * 100 / len(z_sorted))]
    # make_ordering_aux(solution_list, x, y, z, x_range, y_range, z_range, x_sorted, y_sorted, z_sorted)
    #
    # # +x, -y, +z
    # x_range = [x_index * 100 / len(x_sorted), x_range[1]]
    # y_range = [y_range[0], 100 - (y_index * 100 / len(y_sorted))]
    # z_range = [z_index * 100 / len(z_sorted), z_range[1]]
    # make_ordering_aux(solution_list, x, y, z, x_range, y_range, z_range, x_sorted, y_sorted, z_sorted)
    #
    # # -x, +y, +z
    # x_range = [x_range[0], 100 - (x_index * 100 / len(x_sorted))]
    # y_range = [y_index * 100 / len(y_sorted), y_range[1]]
    # z_range = [z_index * 100 / len(z_sorted), z_range[1]]
    # make_ordering_aux(solution_list, x, y, z, x_range, y_range, z_range, x_sorted, y_sorted, z_sorted)

