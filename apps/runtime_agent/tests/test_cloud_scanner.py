from cloud_scanner import scan_cloud_services

def test_scan_cloud_services():
    results = scan_cloud_services("aws", "123456")
    assert isinstance(results, list)
    assert "resource" in results[0]
    assert "vulnerability" in results[0]
