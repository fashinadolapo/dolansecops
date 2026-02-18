from typing import List

class Node:
    def __init__(self, node_id: str, name: str, vulnerability: str, org_id: str):
        self.node_id = node_id
        self.name = name
        self.vulnerability = vulnerability
        self.org_id = org_id
        self.edges: List[str] = []

    def add_edge(self, target_node_id: str):
        if target_node_id not in self.edges:
            self.edges.append(target_node_id)
