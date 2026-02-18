class MultiTenantGraph:
    def __init__(self):
        self.graphs = {}  # org_id -> list of nodes

    def add_node(self, org_id: str, node):
        if org_id not in self.graphs:
            self.graphs[org_id] = []
        self.graphs[org_id].append(node)

    def get_graph(self, org_id: str):
        return self.graphs.get(org_id, [])
