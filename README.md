
# Flask Monitoring with Prometheus

This project demonstrates how to monitor a simple Flask web application using **Prometheus**. The app exposes metrics that Prometheus scrapes, allowing you to track application performance and status. You can extend the monitoring by adding **Grafana** dashboards to visualize these metrics.

---

## 🚀 Features

- Simple Flask web app exposing metrics for Prometheus.
- Prometheus configuration to scrape the Flask app metrics endpoint.
- Dockerized setup for easy deployment.
- (Optional) Instructions to add Grafana for advanced visualization.

---

## 📁 Project Structure

```
monitoring-flask-app/
├── app.py                 # Flask application exposing metrics
├── Dockerfile             # Dockerfile to build the Flask app container
├── requirements.txt       # Python dependencies
├── prometheus.yml         # Prometheus scrape configuration
├── README.md              # Project documentation
```

---

## 🧪 How to Run Locally

### Prerequisites

- Docker installed and running
- (Optional) Docker Compose if running Prometheus + Grafana together

### Build and Run Flask App Container

```bash
docker build -t flask-prometheus-app .
docker run -p 5000:5000 flask-prometheus-app
```

The Flask app will be available at:  
`http://localhost:5000`

---

### Run Prometheus to Scrape Metrics

Run Prometheus container with the config file:

```bash
docker run -p 9090:9090 -v $(pwd)/prometheus.yml:/etc/prometheus/prometheus.yml prom/prometheus
```

Access Prometheus UI at:  
`http://localhost:9090`

---

## 🛠️ Prometheus Configuration (`prometheus.yml`)

```yaml
global:
  scrape_interval: 5s

scrape_configs:
  - job_name: 'flask-app'
    static_configs:
      - targets: ['host.docker.internal:5000']
```

> Note: Use `host.docker.internal` to allow Prometheus container to reach your local Flask app.

---

## 📊 (Optional) Add Grafana for Visualization

You can run Grafana in Docker and connect it to Prometheus as a data source to build dashboards.

```bash
docker run -d -p 3000:3000 grafana/grafana
```

Access Grafana UI at:  
`http://localhost:3000`  
Default login: `admin` / `admin`

Set up Prometheus as a data source in Grafana to visualize your Flask app metrics.

---

## 🔧 Technologies Used

- Python 3.x with Flask
- Prometheus
- Docker
- (Optional) Grafana

---

## 📝 Notes

- Adjust `prometheus.yml` targets depending on your environment (especially if running containers on Linux or Mac).
- Ensure Flask app exposes `/metrics` endpoint correctly for Prometheus scraping.

---

 
## ✉️ patelayush1929@gmail.com 
## ✉️ ayushkumarp.29@gmail.com

For any questions or improvements, feel free to open issues or reach out!

---

**Happy Monitoring!** 🚀
