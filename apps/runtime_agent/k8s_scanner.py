from kubernetes import client, config

def scan_cluster(namespace: str = None):
    config.load_kube_config()
    v1 = client.CoreV1Api()
    pods = v1.list_pod_for_all_namespaces(watch=False)
    results = []
    for pod in pods.items:
        if namespace and pod.metadata.namespace != namespace:
            continue
        results.append({
            "name": pod.metadata.name,
            "namespace": pod.metadata.namespace,
            "vulnerabilities": []  # Integrate Trivy or custom scanner here
        })
    return results
