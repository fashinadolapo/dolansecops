from celery import Celery
from websocket import manager
from cloud_scanner import scan_cloud_services
from infra_scanner import scan_iac
from container_scanner import scan_container

celery_app = Celery(
    "runtime_tasks",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0"
)

@celery_app.task
def ingest_runtime_scans(org_id: str, iac_paths: list, images: list, clouds: dict):
    results = []

    # IaC scans
    for iac in iac_paths:
        results += scan_iac(iac["type"], iac["path"])

    # Container scans
    for image in images:
        results += scan_container(image)

    # Cloud scans
    for cloud, account in clouds.items():
        results += scan_cloud_services(cloud, account)

    # Broadcast live updates
    import asyncio
    asyncio.run(manager.broadcast({
        "event": "runtime_scan",
        "org_id": org_id,
        "results": results
    }))

    return results
