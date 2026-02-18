import boto3

def scan_ecs_clusters(region: str):
    ecs = boto3.client("ecs", region_name=region)
    clusters = ecs.list_clusters()["clusterArns"]
    results = []
    for cluster in clusters:
        tasks = ecs.list_tasks(cluster=cluster)["taskArns"]
        results.append({
            "cluster": cluster,
            "tasks": tasks,
            "vulnerabilities": []  # Integrate Trivy or scanner
        })
    return results
