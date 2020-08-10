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