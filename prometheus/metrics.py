from flask import Flask

app = Flask(__name__)

@app.route('/')
def metrics():
    # Generate metrics
    metrics_data = generate_metrics()
    return metrics_data

def generate_metrics():
    # Generate sample metrics
    cpu_usage = 85.0
    memory_usage = 512
    disk_usage = 30.0

    # Format metrics in Prometheus exposition format
    metrics = [
        '# HELP cpu_usage_total CPU usage in percentage\n',
        '# TYPE cpu_usage_total gauge\n',
        f'cpu_usage_total {cpu_usage}\n',
        '# HELP memory_usage_total Memory usage in MB\n',
        '# TYPE memory_usage_total gauge\n',
        f'memory_usage_total {memory_usage}\n',
        '# HELP disk_usage_total Disk usage in percentage\n',
        '# TYPE disk_usage_total gauge\n',
        f'disk_usage_total {disk_usage}\n'
    ]

    return ''.join(metrics)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)

