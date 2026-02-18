class TenantScanStore:
    def __init__(self):
        self.store = {}  # org_id -> list of scan results

    def add_scan_result(self, org_id: str, result: dict):
        if org_id not in self.store:
            self.store[org_id] = []
        self.store[org_id].append(result)

    def get_results(self, org_id: str):
        return self.store.get(org_id, [])
