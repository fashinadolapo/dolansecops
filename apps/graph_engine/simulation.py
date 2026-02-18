from multi_tenant import MultiTenantGraph

def simulate_attack(org_id: str, graph_store: MultiTenantGraph):
    """
    Traverse the attack graph and calculate risk score.
    """
    graph = graph_store.get_graph(org_id)
    risk_score = 0
    for node in graph:
        severity = node.vulnerability.lower()
        if "critical" in severity:
            risk_score += 10
        elif "high" in severity:
            risk_score += 5
        else:
            risk_score += 1
    return {"org_id": org_id, "risk_score": risk_score, "nodes": len(graph)}
