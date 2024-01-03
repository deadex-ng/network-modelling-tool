"""Implementation of dijkstra's algorithm.
https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/
"""

from typing import List


class Dijkstra:
    def __init__(self, graph):
        self.graph = graph
        self.V = len(graph)
        self.prev = {}

    def print_solution(self, dist):
        print("Vertex \t Distance from Source")
        for node in range(self.V):
            print(node, "\t\t", dist[node])

    def min_distance(self, dist, spt_set):
        # Initialize minimum distance for next node
        min = 1e7

        # Search not nearest vertex not in the
        # shortest path tree
        for v in range(self.V):
            if dist[v] < min and spt_set[v] is False:
                min = dist[v]
                min_index = v
        return min_index

    def shortest_path(self, src: int) -> List[int]:
        """Calculates the shortest path from starting point.

        Args:
        src: int. The starting point.
        """
        dist = [1e7] * self.V
        dist[src] = 0
        spt_set = [False] * self.V
        for cout in range(self.V):
            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.min_distance(dist, spt_set)

            # Put the minimum distance vertex in the
            # shortest path tree
            spt_set[u] = True

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            for v in range(self.V):
                if (
                    self.graph[u][v] > 0
                    and spt_set[v] is False
                    and dist[v] > dist[u] + self.graph[u][v]
                ):
                    if v in self.prev.keys():
                        self.prev[v] = u
                    else:
                        self.prev[v] = u
                    dist[v] = dist[u] + self.graph[u][v]
        return dist

    def traffic_path(self, start_node, dest_node):
        """Get the shortest traffic path between two nodes.

        Args:
        start_node: int. The index of the start node.
        dest_node: int. the index of the destination node.
        """
        path = [dest_node]
        while dest_node != start_node:
            dest_node = self.prev[dest_node]
            path.append(dest_node)
        return path
