class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adjacency_list = [[] for _ in range(num_vertices)]

    def add_edge(self, u, v):
        self.adjacency_list[u].append(v)

    def dfs(self, start_vertex):
        visited = [False] * self.num_vertices
        self._dfs_recursive(start_vertex, visited)

    def _dfs_recursive(self, current_vertex, visited):
        visited[current_vertex] = True
        print(current_vertex, end=" ")

        for neighbor in self.adjacency_list[current_vertex]:
            if not visited[neighbor]:
                self._dfs_recursive(neighbor, visited)


if __name__ == "__main__":
    graph = Graph(6)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(4, 5)

    print("Обход графа с поиском в глубину (DFS):")
    graph.dfs(0)