from container_scanner import scan_container

def test_scan_container_invalid_image():
    results = scan_container("invalid/image:latest")
    assert isinstance(results, list)  # Should not crash
