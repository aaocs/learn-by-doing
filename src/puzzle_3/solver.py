from .pyramid_reader_2d import PyramidReader

FILE_PATH_PREFIX = '/Users/ashley.arain/git-proj/learn-by-doing/src/puzzle_3/res/'
start_vertex = '[1][1]'
end_vertex = '[END]'

# Part 1

pyramid_reader = PyramidReader(FILE_PATH_PREFIX + 'part1.txt')
path, distances, max_distance = pyramid_reader.graph.dijkstra(start_vertex, end_vertex)

print('Part 1:')
print(f"Path: {path}, Distances: {distances}, Maximum Distance: {max_distance}")

# Part 2

pyramid_reader = PyramidReader(FILE_PATH_PREFIX + 'part2.txt')
path, distances, max_distance = pyramid_reader.graph.dijkstra(start_vertex, end_vertex)

print('Part 2:')
print(f"Path: {path}, Maximum Distance: {max_distance}")
