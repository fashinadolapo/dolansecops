class Node:
    def __init__(self, id: str, name: str, asset_type: str, severity: str):
        self.id = id
        self.name = name
        self.asset_type = asset_type
        self.severity = severity
        self.edges = []

    def add_edge(self, edge):
        self.edges.append(edge)
