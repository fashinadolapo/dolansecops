import subprocess
import json

def scan_container(image: str):
    result = subprocess.run(["trivy", "image", "--format", "json", image], capture_output=True)
    return json.loads(result.stdout.decode()) if result.stdout else []
