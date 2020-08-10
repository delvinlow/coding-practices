import unittest

from main import Solution

class TestCriticalConnections(unittest.TestCase):
    def test_single_critical_edge_returns_one(self):
        input_edge_list = [[1, 0], [2, 1], [0, 2], [3, 1]]
        critical_edges = Solution().criticalConnections(4, input_edge_list)
        self.assertEqual(critical_edges, [[1, 3]])

    def test_double_critical_edges_returns_both(self):
        input_edge_list = [[1, 0], [2, 1], [0, 2], [3, 1], [4, 1]]
        critical_edges = Solution().criticalConnections(5, input_edge_list)
        self.assertEqual(critical_edges, [[1, 3], [1, 4]])

    def test_star_graph_returns_all_edges(self):
        input_edge_list = [[1, 0], [2, 1], [3, 1], [4, 1]]
        critical_edges = Solution().criticalConnections(4, input_edge_list)
        self.assertEqual(critical_edges, [[0, 1], [1, 2], [1, 3], [1, 4]])

