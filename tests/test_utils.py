"""Tests for utils/utils.py"""
import sys
import unittest

sys.path.append(".")
from utils.utils import unique


class TestUtils(unittest.TestCase):
    def test_unique(self):
        nodes_list = ["A", "A", "B", "C"]
        actual = unique(nodes_list)
        expected = ["A", "B", "C"]
        self.assertEqual(actual, expected)
