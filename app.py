from flask import Flask, Response
from prometheus_client import Counter, generate_latest, REGISTRY

app = Flask(__name__)

# Define a metric
REQUEST_COUNT = Counter('app_requests_total', 'Total number of requests')

@app.route('/')
def index():
    REQUEST_COUNT.inc()  # Increment metric counter
    return "Hello, Prometheus!"

@app.route('/metrics')
def metrics():
    return Response(generate_latest(REGISTRY), mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
