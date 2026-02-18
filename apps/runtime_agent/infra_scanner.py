import subprocess
import json

def scan_iac(iac_type: str, path: str):
    """
    Scan Infrastructure-as-Code templates
    """
    if iac_type.lower() == "terraform":
        result = subprocess.run(["checkov", "-d", path, "-o", "json"], capture_output=True)
    elif iac_type.lower() == "bicep":
        result = subprocess.run(["azbicep-lint", path, "--json"], capture_output=True)
    elif iac_type.lower() == "cdk":
        result = subprocess.run(["cdk-nag", path, "--json"], capture_output=True)
    else:
        return []
    return json.loads(result.stdout.decode()) if result.stdout else []
