from graph_builder import build_attack_graph, graph_store

def test_build_attack_graph():
    normalized = [
        {"file": "app.py", "description": "SQL Injection", "severity": "high"},
        {"file": "db.py", "description": "Open S3 Bucket", "severity": "critical"}
    ]
    org_id = "org_test"
    graph = build_attack_graph(org_id, normalized)
    assert len(graph) == 2
    assert graph[0].edges[0] == graph[1].node_id
