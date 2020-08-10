class Solution:
    def criticalConnections(self, n, connections):
        adjacency_list = EdgeList(connections).to_adjacency_list()

        critical_edges = []
        vertices = adjacency_list.keys()
        for edge in connections:
            visited = {vertex: False for vertex in vertices}
            connected_components = 0
            for vertex in vertices:
                if visited[vertex] == False:
                    self.dfs(vertex, adjacency_list, visited, edge)
                    connected_components += 1

            if connected_components > 1:
                critical_edges.append(sorted(edge))

        return critical_edges

    def dfs(self, vertex, adjacency_list, visited, ignored_edge):
        visited[vertex] = True
        for neighbour in adjacency_list[vertex]:
            if visited[neighbour] == False and not (
                vertex in ignored_edge and neighbour in ignored_edge
            ):
                self.dfs(neighbour, adjacency_list, visited, ignored_edge)


class EdgeList:
    def __init__(self, edges):
        self.edges = edges

    def to_adjacency_list(self):
        adjacency_list = {}
        for vertex_start, vertex_end in self.edges:
            self.insert_vertex_in_order(adjacency_list, vertex_start, vertex_end)
            self.insert_vertex_in_order(adjacency_list, vertex_end, vertex_start)

        return adjacency_list

    def insert_vertex_in_order(self, adjacency_list, source_vertex, end_vertex):
        existing_neighbours = adjacency_list.setdefault(source_vertex, [])
        existing_neighbours.append(end_vertex)
        adjacency_list[source_vertex] = existing_neighbours
