"""Common utility functions."""

import sys
from functools import reduce
from typing import List

sys.path.append(".")
from graph.dijkstra import Dijkstra


def unique(nodes: List[str]) -> List[str]:
    """Returns a list with unique elemets.

    Args:
    nodes: List[str]. Graph nodes.
    """
    unique_values = reduce(lambda x, y: x + [y] if y not in x else x, nodes, [])
    return unique_values


def model_traffic(
    adj_matrix_graph: List[List],
    starting_point: int,
    finishing_point: int,
    traffic_demand: int,
) -> List[str]:
    """Returns the route of the traffic and it's demand.

    Args:
    adj_matrix_graph: List[List]. The adjacent matrix graph.
    starting_point: int. The starting point for traffic route.
    finishing_point: int. The destination for the traffic route.
    traffic_demand: int. The traffic demand.
    """
    dj = Dijkstra(adj_matrix_graph)
    dist = dj.shortest_path(starting_point)
    path = dj.traffic_path(starting_point, finishing_point)
    return (path, traffic_demand)
