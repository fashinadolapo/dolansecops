from vulnerability_normalizer import normalize_vulnerabilities

def test_normalize_vulnerabilities():
    raw_results = [
        {"tool": "CodeQL", "file": "app.py", "line": 12, "severity": "high", "description": "vuln", "recommendation": "fix it"}
    ]
    normalized = normalize_vulnerabilities(raw_results)
    assert normalized[0]["scanner"] == "codeql"
    assert normalized[0]["category"] == "static_code_analysis"
