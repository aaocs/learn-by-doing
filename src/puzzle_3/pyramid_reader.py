from .graph import Graph

def _add_vertex_data(graph, list_of_lists):
    vertex_counter = 0 # Vertices are 0-indexed.
    for i, row in enumerate(list_of_lists, start=1):
        for j, node in enumerate(row, start=1):
            graph.add_vertex_data(vertex_counter, '[{0}][{1}]'.format(i, j))
            vertex_counter += 1
    graph.add_vertex_data(vertex_counter, '[END]')
    return vertex_counter

class PyramidReader2D:
    def __init__(self, file):
        self.file = file
        self.graph = self._construct_graph()

    def _triangle_number(self, n):
        return n * (n + 1) // 2

    def _construct_graph(self):
        all_rows = []

        input = open(self.file, "r")

        for line in input:
            list = line.rstrip().split(" ")
            all_rows.append(list)

        input.close()

        n = len(all_rows)
        size = self._triangle_number(n) + 1
        graph = Graph(size)

        # Add vertex data.
        vertex_counter = _add_vertex_data(graph, all_rows)

        # Add edges.
        for i, row in enumerate(all_rows, start=1):
            prev_t_num = self._triangle_number(i - 1)
            curr_t_num = self._triangle_number(i)

            for j, node in enumerate(row, start=1):
                # Vertices are 0-indexed.
                if i == len(all_rows):
                    # Connect all nodes on the bottom row to the top node.
                    graph.add_edge(prev_t_num + j - 1, vertex_counter, int(all_rows[0][0], 16))
                else:
                    for k in [j - 1, j]:
                        graph.add_edge(prev_t_num + j - 1, curr_t_num + k, int(all_rows[i][k], 16))

        return graph

class PyramidReader3D:
    def __init__(self, file):
        self.file = file
        self.graph = self._construct_graph()

    def _pyramid_number(self, n):
        return n * (n + 1) * ((2 * n) + 1) // 6

    def _construct_graph(self):
        all_planes = []

        input = open(self.file, "r")

        plane_counter = 1
        prev_plane_size = 0
        plane_size = 1
        current_plane = []
        for line in input:
            list = line.rstrip().split(" ")
            current_plane += list

            if len(current_plane) == plane_size - prev_plane_size:
                all_planes.append(current_plane)
                current_plane = []
                plane_counter += 1
                prev_plane_size = plane_size
                plane_size = self._pyramid_number(plane_counter)

        input.close()

        n = len(all_planes)
        size = self._pyramid_number(n) + 1
        graph = Graph(size)

        # Add vertex data.
        vertex_counter = _add_vertex_data(graph, all_planes)

        # Add edges.
        for i, plane in enumerate(all_planes, start=1):
            prev_p_num = self._pyramid_number(i - 1)
            curr_p_num = self._pyramid_number(i)
            column_counter = -1 # This will equal 0 after the first if-check.

            for j, node in enumerate(plane, start=1):
                # Vertices are 0-indexed.
                if i == len(all_planes):
                    # Connect all nodes on the bottom plane to the top node.
                    graph.add_edge(prev_p_num + j - 1, vertex_counter, int(all_planes[0][0], 16))
                else:
                    if (j - 1) % i == 0:
                        column_counter += 1

                    for k in [
                        column_counter + j - 1,
                        column_counter + j,
                        column_counter + j + i,
                        column_counter + j + i + 1
                    ]:
                        graph.add_edge(prev_p_num + j - 1, curr_p_num + k, int(all_planes[i][k], 16))

        return graph
