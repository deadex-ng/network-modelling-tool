import unittest
import sys

sys.path.append(".")
from graph.graph import Graph
from graph.dijkstra import Dijkstra


class TestGraph(unittest.TestCase):
    def setUp(self) -> None:
        self.graph = Graph()
        self.graph.add_vertex("A")
        self.graph.add_vertex("B")
        self.graph.add_vertex("C")
        self.graph.add_edge("A", "B", 5)
        self.graph.add_edge("B", "C", 5)
        self.graph.add_edge("A", "C", 1)
        self.graph_matrix = self.graph.get_graph()
        self.dijkstra = Dijkstra(self.graph_matrix)

    def test_shortest_path(self) -> None:
        actual = self.dijkstra.shortest_path(0)
        expected = [0, 5, 1]
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
