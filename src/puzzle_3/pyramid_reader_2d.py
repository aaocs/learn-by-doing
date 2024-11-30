from .graph import Graph

class PyramidReader:
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
        vertex_counter = 0 # Vertices are 0-indexed.
        for i, row in enumerate(all_rows, start=1):
            for j, node in enumerate(row, start=1):
                graph.add_vertex_data(vertex_counter, '[{0}][{1}]'.format(i, j))
                vertex_counter += 1

        # Add edges.
        for i, row in enumerate(all_rows, start=1):
            prev_t_num = self._triangle_number(i - 1)
            curr_t_num = self._triangle_number(i)

            for j, node in enumerate(row, start=1):
                # Vertices are 0-indexed.
                if i == len(all_rows):
                    # Connect all nodes on the bottom row to the top node.
                    graph.add_edge(prev_t_num + j - 1, 0, int(all_rows[1][1], 16))
                else:
                    graph.add_edge(prev_t_num + j - 1, curr_t_num + j - 1, int(all_rows[i][j - 1], 16))
                    graph.add_edge(prev_t_num + j - 1, curr_t_num + j, int(all_rows[i][j], 16))


        #print(all_rows)
        return graph
