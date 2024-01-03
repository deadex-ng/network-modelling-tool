import unittest
import sys

sys.path.append(".")

from graph.graph import Graph
from unittest.mock import patch


class TestGraph(unittest.TestCase):
    def setUp(self) -> None:
        self.graph = Graph()

    def test_add_vertex(self) -> None:
        self.graph.add_vertex("A")
        actual = self.graph.get_vertices()
        expected = ["A"]
        self.assertEqual(actual, expected)

    @patch("builtins.print")
    def test_add_vertex_already_exists(self, mock_print) -> None:
        self.graph.add_vertex("A")
        self.graph.add_vertex("A")
        mock_print.assert_called_with("Vertex ", "A", " already exists")

    def test_add_edge(self) -> None:
        self.graph.add_vertex("A")
        self.graph.add_vertex("B")
        self.graph.add_edge("A", "B", 5)
        actual = self.graph.get_weight(0, 1)
        expected = (5, 5)
        self.assertEqual(actual, expected)

    @patch("builtins.print")
    def test_add_edge_node_does_not_exists(self, mock_print) -> None:
        self.graph.add_vertex("A")
        self.graph.add_vertex("B")
        self.graph.add_edge("A", "B", 5)
        self.graph.add_edge("A", "C", 2)
        mock_print.assert_called_with("Vertex ", "C", " does not exist.")


if __name__ == "__main__":
    unittest.main()
