import unittest

from main import EdgeList

class TestEdgeList(unittest.TestCase):
    def test_edge_list_constructor(self):
        input_connections = [[0, 1], [1, 2], [2, 0], [1, 3]]
        network_graph = EdgeList(input_connections)
        self.assertEqual(network_graph.edges, input_connections)


class TestEdgeListConversion(unittest.TestCase):
    def test_edge_list_to_adjacency_list(self):
        input_edge_list = [[0, 1], [1, 2], [2, 0], [1, 3]]
        expected_adjacency_list = {0: [1, 2], 1: [0, 2, 3], 2: [1, 0], 3: [1]}
        output_adjacency_list = EdgeList(input_edge_list).to_adjacency_list()
        self.assertEqual(output_adjacency_list, expected_adjacency_list)

    def test_inverted_edge_list_to_adjacency_list(self):
        input_edge_list = [[1, 0], [2, 1], [0, 2], [3, 1]]
        expected_adjacency_list = {0: [1, 2], 1: [0, 2, 3], 2: [1, 0], 3: [1]}
        output_adjacency_list = EdgeList(input_edge_list).to_adjacency_list()
        self.assertEqual(output_adjacency_list, expected_adjacency_list)

    def test_empty_edge_list_to_adjacency_list(self):
        input_edge_list = []
        expected_adjacency_list = {}
        output_adjacency_list = EdgeList(input_edge_list).to_adjacency_list()
        self.assertEqual(output_adjacency_list, expected_adjacency_list)

    def test_disconnected_edge_list_to_adjacency_list(self):
        input_edge_list = [[1, 2], [3, 5]]
        expected_adjacency_list = {1: [2], 2: [1], 3: [5], 5: [3]}
        output_adjacency_list = EdgeList(input_edge_list).to_adjacency_list()
        self.assertEqual(output_adjacency_list, expected_adjacency_list)

    def test_star_edge_list_to_adjacency_list(self):
        input_edge_list = [[1, 0], [2, 1], [3, 1], [4, 1]]
        expected_adjacency_list = {0: [1], 1: [0, 2, 3, 4], 2: [1], 3: [1], 4: [1]}
        output_adjacency_list = EdgeList(input_edge_list).to_adjacency_list()
        self.assertEqual(output_adjacency_list, expected_adjacency_list)

    def test_two_cycle_connected_with_one_edge_to_adjacency_list(self):
        first_cycle = [[0, 1], [1, 2], [2, 5], [0, 3], [3, 4], [4, 5]]
        second_cycle = [[6, 9], [6, 7], [7, 8], [8, 11], [10, 11], [9, 10]]
        critical_edge = [[5, 6]]
        input_edge_list = first_cycle + second_cycle + critical_edge

        expected_adjacency_list = {0: [1, 3], 1: [0, 2], 2: [1, 5], 3: [0, 4],
            4: [3, 5], 5: [2, 4, 6], 6: [9, 7, 5], 7: [6, 8], 8: [7, 11], 9: [6, 10], 10: [11, 9], 11: [8, 10]}
        output_adjacency_list = EdgeList(input_edge_list).to_adjacency_list()

        self.assertEqual(output_adjacency_list, expected_adjacency_list)