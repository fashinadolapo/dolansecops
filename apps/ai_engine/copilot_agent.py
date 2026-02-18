from vulnerability_normalizer import normalize_vulnerabilities
from patch_generator import generate_patch

class CopilotAgent:
    def __init__(self, org_id: str):
        self.org_id = org_id

    def process_scan_results(self, raw_results):
        normalized = normalize_vulnerabilities(raw_results)
        patches = []
        for vuln in normalized:
            code_snippet = vuln.get("code_snippet", "")
            description = vuln.get("description", "")
            patch = generate_patch(code_snippet, description, self.org_id)
            patches.append({
                "file": vuln.get("file"),
                "line": vuln.get("line"),
                "patch": patch,
                "severity": vuln.get("severity"),
                "category": vuln.get("category")
            })
        return patches
