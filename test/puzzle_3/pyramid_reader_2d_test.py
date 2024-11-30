import unittest
from ...src.puzzle_3.pyramid_reader_2d import PyramidReader

class TestStringMethods(unittest.TestCase):
    FILE_PATH_PREFIX = '/Users/ashley.arain/git-proj/learn-by-doing/src/puzzle_3/res/'

    def test_edge_count_example_1(self):
        pyramid_reader = PyramidReader(self.FILE_PATH_PREFIX + 'example1.txt')
        self.assertEqual(pyramid_reader.graph.edge_count, 11)

    def test_edge_count_part_1(self):
        pyramid_reader = PyramidReader(self.FILE_PATH_PREFIX + 'part1.txt')
        self.assertEqual(pyramid_reader.graph.edge_count, 79)

    def test_maximum_sum_example_1(self):
        pyramid_reader = PyramidReader(self.FILE_PATH_PREFIX + 'example1.txt')

        path, distances, max_distance = pyramid_reader.graph.dijkstra('[1][1]', '[4][4]')
        print(f"Path: {path}, Distances: {distances}, Maximum Distance: {max_distance}")

        self.assertEqual(max_distance, 23)

if __name__ == '__main__':
    unittest.main()
