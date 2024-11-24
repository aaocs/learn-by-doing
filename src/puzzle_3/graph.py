class Graph:
    def __init__(self, size):
        self.adj_matrix = [[None] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size

    def add_edge(self, u, v, weight):
        self.adj_matrix[u][v] = weight

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def get_path(self, predecessors, start_vertex, end_vertex):
        path = []
        current = self.vertex_data.index(end_vertex)
        while current is not None:
            path.insert(0, self.vertex_data[current])
            current = predecessors[current]
            if current == self.vertex_data.index(start_vertex):
                path.insert(0, start_vertex)
                break
        return '->'.join(path)  # Join the vertices with '->'

    def dijkstra(self, start_vertex_data, end_vertex_data):
        start_vertex = self.vertex_data.index(start_vertex_data)
        end_vertex = self.vertex_data.index(end_vertex_data)
        distances = [float('-inf')] * self.size
        predecessors = [None] * self.size
        distances[start_vertex] = 0 # TODO: Use the first vertex value.
        visited = [False] * self.size

        for _ in range(self.size):
            max_distance = float('-inf')
            u = None
            for i in range(self.size):
                if not visited[i] and distances[i] > max_distance:
                    max_distance = distances[i]
                    u = i
                    break

            if u is None or u == end_vertex:
                break

            visited[u] = True

            for v in range(self.size):
                if self.adj_matrix[u][v] is not None and not visited[v]:
                    alt = distances[u] + self.adj_matrix[u][v]
                    if alt > distances[v]:
                        distances[v] = alt
                        predecessors[v] = u

        return self.get_path(predecessors, start_vertex_data, end_vertex_data), distances, distances[end_vertex]
