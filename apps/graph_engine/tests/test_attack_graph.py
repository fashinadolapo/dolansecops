import pytest
from node import Node
from edge import Edge
from attack_graph import AttackGraph

def test_attack_path_simulation():
    g = AttackGraph()
    n1, n2 = Node("1", "app", "service", "high"), Node("2", "db", "service", "medium")
    g.add_node(n1)
    g.add_node(n2)
    g.add_edge(Edge("1", "2", "exploit"))
    paths = g.simulate_attack_path("1")
    assert paths == [["1", "2"]]
