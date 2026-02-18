import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_pr_fix_endpoint():
    response = client.post("/pr/suggest_fix", json={
        "repo_name": "example-repo",
        "file_path": "vuln.py"
    })
    assert response.status_code == 200
    data = response.json()
    assert "ai_fix" in data
    assert "repo" in data
