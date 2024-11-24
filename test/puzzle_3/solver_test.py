import unittest
from ...src.puzzle_3.graph import Graph

class TestStringMethods(unittest.TestCase):

    def test_maximum_sum_example_0(self):
        # Example 0 is the top 3 rows of Example 1.
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

        path, distances, max_distance = g.dijkstra('A', 'G')
        print(f"Path: {path}, Distances: {distances}, Maximum Distance: {max_distance}")

        self.assertEqual(max_distance, 16)

    def test_maximum_sum_example_1(self):
        g = Graph(11)

        g.add_vertex_data(0, 'A')
        g.add_vertex_data(1, 'B')
        g.add_vertex_data(2, 'C')
        g.add_vertex_data(3, 'D')
        g.add_vertex_data(4, 'E')
        g.add_vertex_data(5, 'F')
        g.add_vertex_data(6, 'G')
        g.add_vertex_data(7, 'H')
        g.add_vertex_data(8, 'I')
        g.add_vertex_data(9, 'J')
        g.add_vertex_data(10, 'K')

        g.add_edge(0, 1, 3)
        g.add_edge(0, 2, 4)
        g.add_edge(1, 3, 2)
        g.add_edge(1, 4, 1)
        g.add_edge(2, 4, 1)
        g.add_edge(2, 5, 7)
        g.add_edge(3, 6, 0xc)
        g.add_edge(3, 7, 0xd)
        g.add_edge(4, 7, 0xd)
        g.add_edge(4, 8, 2)
        g.add_edge(5, 8, 2)
        g.add_edge(5, 9, 5)

        start_weight = 5
        g.add_edge(6, 10, start_weight)
        g.add_edge(7, 10, start_weight)
        g.add_edge(8, 10, start_weight)
        g.add_edge(9, 10, start_weight)

        path, distances, max_distance = g.dijkstra('A', 'K')
        print(f"Path: {path}, Distances: {distances}, Maximum Distance: {max_distance}")

        self.assertEqual(max_distance, 23)

if __name__ == '__main__':
    unittest.main()
