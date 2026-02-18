from node import Node
from edge import Edge

class AttackGraph:
    def __init__(self):
        self.nodes = {}
        self.edges = []

    def add_node(self, node: Node):
        self.nodes[node.id] = node

    def add_edge(self, edge: Edge):
        if edge.source in self.nodes and edge.target in self.nodes:
            self.edges.append(edge)
            self.nodes[edge.source].add_edge(edge)
        else:
            raise ValueError("Source or target node not found")

    def simulate_attack_path(self, start_node_id: str, max_depth=5):
        paths = []
        self._dfs(start_node_id, [], paths, max_depth)
        return paths

    def _dfs(self, current_node_id, path, paths, max_depth):
        if len(path) > max_depth:
            return
        path.append(current_node_id)
        current_node = self.nodes[current_node_id]
        if not current_node.edges:
            paths.append(list(path))
        for edge in current_node.edges:
            self._dfs(edge.target, path, paths, max_depth)
        path.pop()
