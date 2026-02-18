import pytest
from patch_generator import generate_patch

def test_generate_patch_returns_string():
    patch = generate_patch("vulnerable_code()", "SQL injection", "org_123")
    assert isinstance(patch, str)
    assert len(patch) > 0
