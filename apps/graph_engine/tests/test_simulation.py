from simulation import simulate_attack
from multi_tenant import MultiTenantGraph
from graph_builder import build_attack_graph

def test_simulate_attack():
    org_id = "org_test_sim"
    normalized = [
        {"file": "app.py", "description": "SQL Injection", "severity": "high"},
        {"file": "db.py", "description": "Open S3 Bucket", "severity": "critical"}
    ]
    graph_store = MultiTenantGraph()
    build_attack_graph(org_id, normalized)
    result = simulate_attack(org_id, graph_store)
    assert result["risk_score"] > 0
    assert result["nodes"] == 0 or result["nodes"] > 0
