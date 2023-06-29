import random
from typing import Dict

import networkx as nx
import numpy as np
import numpy.typing as npt
from dsutil import segment


def locate_on_2D_space(
    vector: npt.ArrayLike, tree: nx.DiGraph,
    layout: Dict[int, npt.ArrayLike], scaler: float = 0
):
    """Locate a vector on the 2D space based on the layout (edge positions)."""
    # associate the vecter with the nearest edge and record the distance
    edge_positions = [
        (tree.nodes[begin]['position'], tree.nodes[end]['position'])
        for begin, end in tree.edges
    ]
    distances = [
        segment.distance(vector, positions)
        for positions in edge_positions
    ]
    edge = np.argmin(distances)
    begin, end = list(tree.edges)[edge]
    distance = np.min(distances)

    # compute the fraction of the projection on the edge, fraction range [0, 1],
    # 0 means the projection is on the begin node, 1 means on the end node
    factor = segment.projection_factor(
        vector, edge_positions[edge], fixed_range=True)
    # locate the nearest point of the edge on the 2D layout
    point = layout[begin] + (layout[end] - layout[begin]) * factor

    # place the point orthogonal on a random direction with the scaled distance
    direction = random.choice([-1, 1])
    vector = layout[end] - layout[begin]
    perpendicular_vector = (-vector[1] * direction, vector[0] * direction)
    perpendicular_unit = (
        perpendicular_vector / np.linalg.norm(perpendicular_vector)
    )
    return point + perpendicular_unit * distance * scaler
