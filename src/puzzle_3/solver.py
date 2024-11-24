# Graph data - Example 0

g = Graph(7)

g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_vertex_data(4, 'E')
g.add_vertex_data(5, 'F')
g.add_vertex_data(6, 'G')

g.add_edge(0, 1, 3)
g.add_edge(0, 2, 4)
g.add_edge(1, 3, 2)
g.add_edge(1, 4, 1)
g.add_edge(2, 4, 1)
g.add_edge(2, 5, 7)

start_weight = 5
g.add_edge(3, 6, start_weight)
g.add_edge(4, 6, start_weight)
g.add_edge(5, 6, start_weight)

# Runner

distance, path = g.dijkstra('A', 'G')
print(f"Path: {path}, Distance: {distance}")
