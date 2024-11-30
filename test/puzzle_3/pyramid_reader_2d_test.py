import unittest
from ...src.puzzle_3.pyramid_reader_2d import PyramidReader

class TestStringMethods(unittest.TestCase):

    def test_edge_count_example_1(self):
        pyramid_reader = PyramidReader('example1.txt')
        self.assertEqual(pyramid_reader.graph.edge_count, 11)

    def test_edge_count_part_1(self):
        pyramid_reader = PyramidReader('part.txt')
        self.assertEqual(pyramid_reader.graph.edge_count, 79)

if __name__ == '__main__':
    unittest.main()
