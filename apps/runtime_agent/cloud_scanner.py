import subprocess
import json

def scan_iac(iac_type: str, path: str):
    """
    Scan Infrastructure-as-Code templates (Terraform/CDK/Bicep)
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

def scan_containers(image: str):
    """
    Scan Docker/container images
    """
    result = subprocess.run(["trivy", "image", "--format", "json", image], capture_output=True)
    return json.loads(result.stdout.decode()) if result.stdout else []

def scan_cloud_services(cloud: str, account_id: str):
    """
    Scan runtime cloud resources (multi-cloud)
    """
    # Placeholder - integrate with AWS, Azure, GCP SDKs
    return [{"resource": "s3_bucket", "vulnerability": "public_read"}]
