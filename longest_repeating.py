import Trie

trie = Trie()

class SubstringTree(object):
    def init(self, string):
        self.string = ""
        self.edge_ids = {}

    def parse_file(self, filename):
        f = open(filename)
        for line in f:
            line = re.sub('\n', '', line)
            line_args = [re.sub('node', '', a) for a in line.split(" ")]
            self.parse_edge(*line_elts)

    def parse_edge(self, id, child, start, end):
        #TODO






class Edge(object):
    def init(self, id, start, end, childs):
        self.id = id
        self.start = start
        self.end = end
        self.childs = []

    def add_child(self, edge):
        self.childs.append(edge)
