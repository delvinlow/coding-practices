import unittest

from main import Solution

class TestCriticalConnections(unittest.TestCase):
    def test_single_critical_edge_returns_one(self):
        input_edge_list = [[1, 0], [2, 1], [0, 2], [3, 1]]
        critical_edges = Solution().criticalConnections(4, input_edge_list)
        self.assertEqual(critical_edges, [[1, 3]])

    def test_single_critical_edge_two_nodes_returns_one(self):
        input_edge_list = [[0, 1]]
        critical_edges = Solution().criticalConnections(1, input_edge_list)
        self.assertEqual(critical_edges, [[0, 1]])

    def test_double_critical_edges_returns_both(self):
        input_edge_list = [[1, 0], [2, 1], [0, 2], [3, 1], [4, 1]]
        critical_edges = Solution().criticalConnections(5, input_edge_list)
        self.assertEqual(critical_edges, [[1, 3], [1, 4]])

    def test_fully_connected_triangle_graph_returns_none(self):
        input_edge_list = [[0, 1], [1, 2], [2, 0]]
        critical_edges = Solution().criticalConnections(3, input_edge_list)
        self.assertEqual(critical_edges, [])

    def test_star_graph_returns_all_edges(self):
        input_edge_list = [[1, 0], [2, 1], [3, 1], [4, 1]]
        critical_edges = Solution().criticalConnections(4, input_edge_list)
        self.assertEqual(critical_edges, [[0, 1], [1, 2], [1, 3], [1, 4]])

    def test_two_cycle_connected_with_one_edge_returns_the_critical_edge(self):
        first_cycle = [[0, 1], [1, 2], [2, 5], [0, 3], [3, 4], [4, 5]]
        second_cycle = [[6, 9], [6, 7], [7, 8], [8, 11], [10, 11], [9, 10]]
        critical_edge = [[5, 6]]
        input_edge_list = first_cycle + second_cycle + critical_edge

        critical_edges = Solution().criticalConnections(13, input_edge_list)

        self.assertEqual(critical_edges, [[5, 6]])