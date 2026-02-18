from models import Node
from multi_tenant import MultiTenantGraph
import uuid

graph_store = MultiTenantGraph()

def build_attack_graph(org_id: str, normalized_vulns: list):
    """
    Build a simple attack graph for given vulnerabilities.
    """
    nodes = []
    for vuln in normalized_vulns:
        node_id = str(uuid.uuid4())
        node = Node(
            node_id=node_id,
            name=vuln.get("file", "unknown"),
            vulnerability=vuln.get("description", "unknown"),
            org_id=org_id
        )
        nodes.append(node)
        graph_store.add_node(org_id, node)

    # Simple connection: sequential dependencies
    for i in range(len(nodes) - 1):
        nodes[i].add_edge(nodes[i+1].node_id)

    return graph_store.get_graph(org_id)
