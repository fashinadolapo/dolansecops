from infra_scanner import scan_iac

def test_scan_iac_empty_path():
    results = scan_iac("terraform", "./nonexistent")
    assert results == []  # Should handle missing path gracefully
