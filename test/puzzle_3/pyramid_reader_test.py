import unittest
from ...src.puzzle_3.pyramid_reader import PyramidReader2D

class TestStringMethods(unittest.TestCase):
    FILE_PATH_PREFIX = '/Users/ashley.arain/git-proj/learn-by-doing/src/puzzle_3/res/'

    def test_graph_size_example_1(self):
        pyramid_reader = PyramidReader2D(self.FILE_PATH_PREFIX + 'example1.txt')
        self.assertEqual(len(pyramid_reader.graph.vertex_data), 11)

    def test_graph_size_part_1(self):
        pyramid_reader = PyramidReader2D(self.FILE_PATH_PREFIX + 'part1.txt')
        self.assertEqual(len(pyramid_reader.graph.vertex_data), 79)

    def test_maximum_sum_example_1(self):
        pyramid_reader = PyramidReader2D(self.FILE_PATH_PREFIX + 'example1.txt')

        path, distances, max_distance = pyramid_reader.graph.dijkstra('[1][1]', '[END]')
        print(f"Path: {path}, Distances: {distances}, Maximum Distance: {max_distance}")

        self.assertEqual(max_distance, 23)

if __name__ == '__main__':
    unittest.main()
