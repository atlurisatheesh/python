from collections import defaultdict

metrics = defaultdict(int)

def record_metric(name: str):
    metrics[name] += 1

def get_metrics():
    return metrics
