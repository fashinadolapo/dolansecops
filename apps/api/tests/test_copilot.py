import pytest
from fastapi.testclient import TestClient
from main import app
from unittest.mock import patch

client = TestClient(app)

@patch("routers.copilot.generate_ai_fix")
def test_suggest_fix(mock_generate):
    mock_generate.return_value = "fixed_code_snippet"
    response = client.post("/copilot/suggest_fix", json={
        "repo_name": "example-repo",
        "file_path": "vuln.py"
    })
    assert response.status_code == 200
    assert response.json()["ai_fix"] == "fixed_code_snippet"
