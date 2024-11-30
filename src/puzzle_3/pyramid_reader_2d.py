from .graph import Graph

class PyramidReader:
    def __init__(self, file):
        self.file = file
        self.graph = self._construct_graph()

    def _construct_graph(self):
        return Graph(1) #TODO.
